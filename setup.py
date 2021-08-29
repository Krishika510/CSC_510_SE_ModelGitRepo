####TODO:
#1 Read long description from README.md and set long_description_content_type='text/markdown'

#2 Check if we need to add all team members as authors here. Stackoverflow say no:
# https://stackoverflow.com/questions/9999829/how-to-specify-multiple-authors-emails-in-setup-py


from setuptools import setup

setup(
		name="MathFun",
		version="0.1",
		description="This module has some fun math functions (Fibonaci, Factorial, Prime)",
		author="Krishika Shivnani",
		author_email="krishika510@gmail.com",
		url="https://github.com/Krishika510/MathFun",
		license="MIT",
		packages=["MathFun"],
		long_description="""\
				This module contains some fun math functions:
						* Fibonacci
						* Factorial
						* Prime
		""",
		classifiers=[
			"Liscence :: SOME LISCENCE",
			"Programming Language :: Python",
			"Development Status :: 1 - Planning",
			"Intended Audience :: Developers",
			"License :: OSI Approved :: MIT License",
			"Topic :: Education"
		],
		keywords="fibonacci factorial prime"
		install_requires=[]
	)