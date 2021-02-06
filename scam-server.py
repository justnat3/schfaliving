# imports
import os
import sys
import time
from selenium import webdriver


# funny funny quirky.
class Scam:
    ...


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)


iteration = 0


def scam_time() -> Scam:
    global iteration
    print("INFO: Vote INT:", iteration)
    # load driver
    print("INFO: OPEN_CHROME_DRIVER")
    opts = webdriver.ChromeOptions()
    opts.add_argument("--headless")
    opts.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(
        resource_path("./driver/chromedriver.exe"), chrome_options=opts
    )
    # go to macky'd's highschool website
    print("INFO: OPEN_SITE_VYPE")
    driver.get(
        "http://northeast.vypetv.com/hubs/grand-lake/area-news/744-vote-now-neok-area-preseason-most-outstanding-girls-soccer-player-presented-by-northeast-tech-poll-ends-2-10.html?fbclid=IwAR1MCG_p_1ee1mMtOFE3zll5PI0KyMsbQCK34XjND1b6XfZhdNUhvER-0TE"
    )
    print("INFO: SELECT_ELEMENT_BY_ID_PDI49601961")
    # click on macky'd's name
    driver.find_element_by_id("PDI_answer49601961").click()
    # click on vote button
    print("INFO: SELECT_ELEMENT_BY_ID_VOTE_BUTTON")
    driver.find_element_by_id("pd-vote-button10735084").click()
    # sleep for 5 seconds

    time.sleep(5)
    print("INFO: CLOSING_CUSTOM_CHROME_DRIVER")
    driver.close()
    driver.quit()
    iteration += 1
    print("\n")
    return


def scam_position() -> Scam:
    while True:
        scam_time()


if __name__ == "__main__":
    scam_position()
