from flask import Blueprint, render_template, request
import re

from src.core.prompts import questions, get_prompt
from src.core.gemini import gemini_response

bp = Blueprint("pages", __name__)

@bp.route("/")
def home():
    return render_template("pages/home.html")

