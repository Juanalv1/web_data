{
    'name': 'Web Data',
    'version': '3.6',
    'category': 'Marketing/Surveys',
    'depends': ['base', 'website'],

    'data': [
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/view.xml',
        'views/menu.xml',
        'data/ir_cron.xml',
    ],
    
    'installable': True,
    'application': True,
    'sequence': 220,
    'license': 'LGPL-3',
}
