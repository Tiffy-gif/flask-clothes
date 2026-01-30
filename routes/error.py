from app import app
from flask import render_template


# Erorr returning files Json

# @app.errorhandler(403)
# def forbidden(e):
#     return jsonify(error="Forbidden",
#                    message="You don't have permission to access this resource."), 403
#
# @app.errorhandler(404)
# def not_found(e):
#     return jsonify(error="Not Found",
#                    message="The requested resource was not found."), 404
#
#
# @app.errorhandler(500)
# def internal_error(e):
#     return jsonify(error="Internal Server Error",
#                    message="Something went wrong on our end."), 500


#
# @app.route('/secret')
# def secret():
#     abort(403)

# @app.route("/admin")
# def test_403():
#     return "Forbidden route", 403



# Error returning pages custome HTMl

@app.errorhandler(404)
def error_404(e):
    return render_template('page_error/404.html')


@app.errorhandler(500)
def error_500(e):
    return render_template('page_error/500.html')



@app.errorhandler(Exception)
def global_error(e):
    return f"<center>Error : {e}</center>"
