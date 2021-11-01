from flask import Blueprint, make_response, request
import plotly.express as px
import pandas as pd

charts_router = Blueprint('charts', __name__)


@charts_router.route('/chart')
def index():
    a = request.args.get('a', default=0)
    c = request.args.get('c', default=0)
    r = request.args.get('r', default=0)
    t = request.args.get('t', default=0)
    e = request.args.get('e', default=0)
    app = request.args.get('app', default=0)
    u = request.args.get('u', default=0)
    co = request.args.get('co', default=0)
    df = pd.DataFrame(dict(
        r=[a, c, r, t, e, app, u, co],
        theta=['A (doc)', 'C (clause)', 'R (Requirement)', 'T (Term)', 'E (errorenous doc)', 'App (Applicability)',
               'U (unspecified requirement)', 'Co (concept)']))
    fig = px.line_polar(df, r='r', theta='theta', line_close=True)
    fig.update_traces(fill='toself')
    response = make_response(fig.to_image(format="png"))
    response.headers.set('Content-Type', 'image/png')
    response.headers.set(
        'Content-Disposition', 'attachment', filename='chart.png')
    return response
