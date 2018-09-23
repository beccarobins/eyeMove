import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

# Add external dependencies using"
# install_requires
# specify version
# package>=#.#
	
setuptools.setup(
	name='eyeMove',
	version='0.0.1',
	description='A package for analyzing eye movements.',
	url='http://github.com/beccarobins/eyeMove',
	author='Becca Robins',
	author_email='becca.k.robins@gmail.com',
	long_description=long_description,
	long_description_content_type="text/markdown",
	packages=setuptools.find_packages(),
	classifiers=(
	"Programming Language :: Python :: 3", 
	"License :: I don't know a thing about package licensing", 
	"Operating System :: OS Independent"),
	license="MIT"
	#install_requires=['']
	)
      #packages=['eyeMove'])
	  #include_package_data=True,
      #zip_safe=False)
