from setuptools import setup, find_packages

setup(
    name='google_ai',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'google-generativeai',
    ],
    entry_points='''
        [console_scripts]
        chat=google_ai.chat:main
    ''',
    project_urls={
        'GitHub': 'https://github.com/horizonbymuneeb/google_generativeai',
    },
)
