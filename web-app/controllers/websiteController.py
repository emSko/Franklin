from flask import Blueprint, render_template, request

website_controller = Blueprint('website_controller', __name__)


@website_controller.route('/sh')
def fun():
    return render_template('index.html')
