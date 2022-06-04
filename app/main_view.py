from flask import Blueprint, render_template, request

main = Blueprint('main', __name__)


@main.route('/')
def welcome():
    return render_template('main/welcome.html')


@main.route('/photobooth')
def photobooth():
    return render_template('main/photobooth.html')


@main.route('/gallery')
def gallery():
    return render_template('main/gallery.html')


@main.route('/portal')
def portal():
    return render_template('main/portals/portalAR.html')


@main.route('/environment')
def enviroment():
    return render_template('main/portals/enviroment.html')


@main.route('/photo360')
def photo360():
    portal_id = int(request.args.get('portal'))
    photos = ["https://cdn.glitch.global/e16f5e56-c882-4834-a302-29605aaa4e28/baikal-1-min.jpg?v=1644759629016",
              "https://cdn.glitch.global/e16f5e56-c882-4834-a302-29605aaa4e28/baikal-2-min.jpg?v=1644759630812", 
              "https://cdn.glitch.global/e16f5e56-c882-4834-a302-29605aaa4e28/baikal-3-min.jpg?v=1644759856208"]
    return render_template('main/portals/360photo.html', photo=photos[portal_id-1], photo_id=portal_id)
