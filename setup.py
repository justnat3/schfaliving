setup(
    name="ScammingHighschools",
    version="1.0.0",
    description="Scamming a highschool because its fun",
    author="justnate",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    install_requires=[
        "selenium", "webdriver-manager", "time"
    ],
    entry_points={"console_scripts": ["scamm=scam:scam_position"]},
)