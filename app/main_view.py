from flask import Blueprint, render_template, request, redirect, url_for
from .logic.stat_computing import get_entities_rating, get_rooms_visiting

main = Blueprint('main', __name__)


@main.route('/')
def welcome():
    return render_template('welcome.html')


@main.route('/guide')
def guide():
    return render_template('start_page.html')


@main.route('/photobooth')
def photobooth():
    return "photobooth"


@main.route('/gallery')
def gallery():
    return 'gallery'


@main.route('/portal')
def portal():
    return 'portal'
