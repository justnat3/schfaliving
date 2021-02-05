# imports
import os
import sys
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


# funny funny quirky.
class Scam:
    ...


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)


def scam_time() -> Scam:
    # load driver
    driver = webdriver.Chrome(resource_path("./driver/winchromedriver.exe"))
    # go to macky'd's highschool website
    driver.get(
        "http://northeast.vypetv.com/hubs/grand-lake/area-news/744-vote-now-neok-area-preseason-most-outstanding-girls-soccer-player-presented-by-northeast-tech-poll-ends-2-10.html?fbclid=IwAR1MCG_p_1ee1mMtOFE3zll5PI0KyMsbQCK34XjND1b6XfZhdNUhvER-0TE"
    )
    # click on macky'd's name
    driver.find_element_by_id("PDI_answer49601961").click()
    # click on vote button
    driver.find_element_by_id("pd-vote-button10735084").click()
    # sleep for 5 seconds
    time.sleep(5)
    driver.close()


def scam_position() -> Scam:
    while True:
        scam_time()
    # Position is different
    # ID is the same everytime
    # PDI_answer49601961
    # PDI_answer49601961
scam_position()
