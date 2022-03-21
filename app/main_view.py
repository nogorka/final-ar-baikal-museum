from flask import Blueprint, render_template, request, redirect, url_for

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


@main.route('/statistics')
def statistics(): 
    return 'statistics'

