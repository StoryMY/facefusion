from facefusion.types import Locales

LOCALES : Locales =\
{
	'en':
	{
		'help':
		{
			'model': 'choose the model responsible for restoring the expression',
			'factor': 'expression transfer strength (0-100 maps to 0-1.2; 83 is approximately full transfer)',
			'source': 'take expression from the original target or the largest face in the first source image',
			'areas': 'choose the items used for the expression areas (choices: {choices})'
		},
		'uis':
		{
			'model_dropdown': 'EXPRESSION RESTORER MODEL',
			'source_dropdown': 'EXPRESSION SOURCE',
			'factor_slider': 'EXPRESSION RESTORER FACTOR',
			'areas_checkbox_group': 'EXPRESSION RESTORER AREAS'
		}
	}
}
