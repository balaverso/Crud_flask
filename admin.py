from flask_admin.contrib.sqla import ModelView
from models import Moeda, Trade, Indicador
from app import db


class MoedaView(ModelView):
    column_editable_list = ('name', 'var', 'vol', 'trades' )
    form_edit_rules = {'name', 'var', 'vol', 'trades', 'indicadores'}
    column_searchable_list = ['name']
    edit_modal = True



    inline_models = [Indicador]

    column_filters = ['name', 'indicadores']
    column_list = ["name", "var", "vol", "indicadores"]


def init_app(admin):
    admin.add_view(MoedaView(Moeda, db.session))
    admin.add_view(ModelView(Trade, db.session))

