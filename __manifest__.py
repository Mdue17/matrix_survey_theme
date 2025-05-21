{
    'name': 'Matrix Survey Theme',
    'version': '1.0',
    'summary': 'Custom CSS for Survey Matrix Table',
    'category': 'Survey',
    'depends': ['survey','web'],
    'data': [],
    'assets': {
        'web.assets_frontend': [
            'matrix_survey_theme/static/src/scss/matrix_survey_frontend.scss',
        ],

    },
    'installable': True,
    'application': False,
}
