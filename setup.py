from setuptools import setup

setup(
    name='xai_transformers',
    version='0.0.1',
    package_dir={'xai_transformers':'src'},
    packages=['xai_transformers.SST', 
    	      'xai_transformers.IMDB', 
    	      'xai_transformers'],
    install_requires=['datasets == 2.3.2',
                      'matplotlib == 3.5.2',
                      'networkx == 2.8.4',
                      'numpy == 1.22.3',
                      'pandas == 1.4.2',
                      'scikit_learn == 1.1.0',
                      'seaborn == 0.11.2',
                      'setuptools == 61.2.0',
                      'torch == 1.11.0',
                      'tqdm == 4.64.0',
                      'transformers == 4.19.0'],
    url='',
    license='',
    author='AmeenAli, oeberle',
    author_email='ameenali@mail.tau.ac.il, oliver.eberle@tu-berlin.de',
    description='The code for the paper XAI for Transformers: Better Explanations through Conservative Propagation, doi'
)
