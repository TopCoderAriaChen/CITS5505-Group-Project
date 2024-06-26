import click
from flask import Flask, render_template, url_for
from exts import db, mail, cache, csrf, avatars
import config
from flask_migrate import Migrate
from blueprints.cms import bp as cms_bp
from blueprints.front import bp as front_bp
from blueprints.user import bp as user_bp
from blueprints.media import bp as media_bp
import commands
from bbs_celery import make_celery
import hooks
import filters
import logging

def create_app(config_class=config.DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    mail.init_app(app)
    cache.init_app(app)
    avatars.init_app(app)

    # Set log level
    app.logger.setLevel(logging.INFO)

    # CSRF protection
    csrf.init_app(app)

    migrate = Migrate(app, db)

    # Register blueprints
    app.register_blueprint(cms_bp)
    app.register_blueprint(front_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(media_bp)

    # Add command
    app.cli.command("create-permission")(commands.create_permission)
    app.cli.command("create-role")(commands.create_role)
    app.cli.command("create-test-front")(commands.create_test_user)
    app.cli.command("create-board")(commands.create_board)
    app.cli.command("create-test-post")(commands.create_test_post)
    app.cli.command("create-admin")(commands.create_admin)

    # Build celery
    celery = make_celery(app)

    # Add hook function
    app.before_request(hooks.bbs_before_request)
    app.errorhandler(401)(hooks.bbs_401_error)
    app.errorhandler(404)(hooks.bbs_404_error)
    app.errorhandler(500)(hooks.bbs_500_error)

    # Add template filter
    app.template_filter("email_hash")(filters.email_hash)

    return app
