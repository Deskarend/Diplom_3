MAIN_URL = 'https://stellarburgers.nomoreparties.site/'


class EndPoints:
    ACCOUNT_PAGE_ENDPOINT = 'account/profile'
    FORGOT_PASSWORD_PAGE_ENDPOINT = 'forgot-password'
    LOGIN_PAGE_ENDPOINT = 'login'
    ORDER_FEED_PAGE_ENDPOINT = 'feed'


class PageUrls:
    MAIN_PAGE_URL = MAIN_URL
    ACCOUNT_PAGE_URL = MAIN_URL + EndPoints.ACCOUNT_PAGE_ENDPOINT
    FORGOT_PASSWORD_PAGE_URL = MAIN_URL + EndPoints.FORGOT_PASSWORD_PAGE_ENDPOINT
    LOGIN_PAGE_URL = MAIN_URL + EndPoints.LOGIN_PAGE_ENDPOINT
    ORDER_FEED_PAGE_URL = MAIN_URL + EndPoints.ORDER_FEED_PAGE_ENDPOINT
