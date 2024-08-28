from flask import Blueprint, render_template, request
import re
import json
from src.core.prompts import questions, get_prompt
from src.core.gemini import gemini_response
from flask import jsonify

bp = Blueprint("pages", __name__)



def format_response(response) -> dict:
    """Formats the Gemini API response into a dictionary for JSON response."""
    ans = {}
    
    # Extract text from the response object
    res_text = response.text if hasattr(response, 'text') else response  # Adjust based on actual response structure
    print(res_text)
    # Define keywords and patterns to dynamically locate sections
    mbti_keyword = '**Likely MBTI Type:**'
    personality_keyword = '**Personality:**'
    handling_keyword = '**How They Handle Situations:**'
    other_traits_keyword = '**Other Personality Traits:**'
    examples_keyword = '**Examples of Situations and Handling Strategies:**'

    # Find the starting index for each section
    mbti_start = res_text.find(mbti_keyword)
    personality_start = res_text.find(personality_keyword)
    handling_start = res_text.find(handling_keyword)
    other_traits_start = res_text.find(other_traits_keyword)
    examples_start = res_text.find(examples_keyword)

    if mbti_start != -1:
        mbti_end = res_text.find('\n\n', mbti_start) if personality_start != -1 else len(res_text)
        ans['MBTI Type'] = res_text[mbti_start + len(mbti_keyword):mbti_end].strip()

    if personality_start != -1:
        personality_end = min([idx for idx in [handling_start, other_traits_start, examples_start] if idx != -1], default=len(res_text))
        ans['Personality Description'] = res_text[personality_start + len(personality_keyword):personality_end].strip()

    if handling_start != -1:
        handling_end = min([idx for idx in [other_traits_start, examples_start] if idx != -1], default=len(res_text))
        handling_text = res_text[handling_start + len(handling_keyword):handling_end].strip()
        situations = {}
        situation_sections = handling_text.split('\n\n')
        for section in situation_sections:
            if section.strip():
                parts = section.split(':', 1)
                if len(parts) == 2:
                    situation_title = parts[0].strip()
                    situation_desc = parts[1].strip()
                    situations[situation_title] = situation_desc
        ans['Handling Situations'] = situations

    if other_traits_start != -1:
        other_traits_end = examples_start if examples_start != -1 else len(res_text)
        other_traits_text = res_text[other_traits_start + len(other_traits_keyword):other_traits_end].strip()
        traits = {}
        traits_sections = other_traits_text.split('\n\n')
        for section in traits_sections:
            if section.strip():
                parts = section.split(':', 1)
                if len(parts) == 2:
                    trait_title = parts[0].strip()
                    trait_desc = parts[1].strip()
                    traits[trait_title] = trait_desc
        ans['Other Personality Traits'] = traits

    if examples_start != -1:
        examples_end = len(res_text)
        examples_text = res_text[examples_start + len(examples_keyword):examples_end].strip()
        examples = {}
        examples_sections = examples_text.split('\n\n')
        for section in examples_sections:
            if section.strip():
                parts = section.split(':', 1)
                if len(parts) == 2:
                    example_title = parts[0].strip()
                    example_desc = parts[1].strip()
                    examples[example_title] = example_desc
        ans['Examples of Situations and Handling Strategies'] = examples

    # Ensure all keys exist in the dictionary
    ans.setdefault('Handling Situations', {})
    ans.setdefault('Other Personality Traits', {})
    ans.setdefault('Examples of Situations and Handling Strategies', {})

    # Convert the response dictionary to JSON format
    return json.dumps(ans)


@bp.route("/")
def home():
    return render_template("pages/home.html")


@bp.route("/explore", methods=['GET', 'POST'])
def explore():
    ques = questions()
    return render_template("pages/explore.html", question = ques)

@bp.route("/personality", methods=['GET', 'POST'])
def personality():
    if request.method == 'POST':
        ans1 = request.form.get('ques1')
        ans2 = request.form.get('ques2')
        ans3 = request.form.get('ques3')
        ans4 = request.form.get('ques4')
        ans5 = request.form.get('ques5')

        prompt = get_prompt([ans1, ans2, ans3, ans4, ans5])
        response = gemini_response(prompt)
        formatted_res = format_response(response)

        # Convert the pretty-printed JSON into a dictionary if it's in string form
        if isinstance(formatted_res, str):
            formatted_res = json.loads(formatted_res)
        
        # Clean up any unwanted markdown syntax
        for key in formatted_res:
            if isinstance(formatted_res[key], str):
                # Remove markdown asterisks or any other unwanted characters
                formatted_res[key] = formatted_res[key].replace('** *', '').replace('**', '')

    return render_template("pages/personality.html", res=formatted_res)
