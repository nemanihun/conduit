class Users:
    user_data = {
        'user': 'user1test20230313',
        'email': 'userteszt@gmail.com',
        'password': 'Teszt2023#'
    }

    user2_data = {
        'user': 'user2test20230313',
        'email': 'user2@gmail.com',
        'password': 'Teszt2023#'
    }

    bad_user_email = {
        'user': 'user2test20230313',
        'email': 'userteszt1@gmail',
        'password': 'Teszt2023#'
    }

    bad_user_password = {
        'user': 'user2test20230313',
        'email': 'userteszt1@gmail.com',
        'password': 'tesztteszt'
    }

    user4_data = {
        'user': 'user3test20230313',
        'email': 'user3@gmail.com',
        'password': 'Teszt2023#'
    }


class Articles:
    article1_data = {
        'Article title': 'Ez egy teszt cikk',
        'What this article about?': 'Ez egy teszt cikk',
        'Write your article': 'Az ajtóra szerelhető rolós szúnyogháló kizárólag alumínium kivitelben érhető el. A megszokott oldalra nyíló szúnyogháló keretekkel ellentétben nem foglal helyet. Az alumínium alkatrészek kérhetők fehérre festve vagy aranytölgy, dió fóliával is. UV stabil üvegszálerősítésű háló biztosítja a tartósságot és a szabad átláthatóságot rögzítet állapotban is.',
        'Enter tags': 'szúnyogháló, alumínium, ajtóra'
    }

    article2_data = {
        'Article title': 'Ez a 2. teszt cikk',
        'What this article about?': 'Ez egy újabb teszt cikk',
        'Write your article': 'Az ajtóra való alumínium rolós szúnyogháló amennyiben teljesen vissza van engedve az egyik oldalon elhelyezett alumínium tokba akkor szabad átjárást biztosít az erkélyajtón. Oldalra húzva és a mágnes segítségével rögzítve pedig tökéletes védelmet nyújt a kellemetlen szúnyogok ellen.',
        'Enter tags': 'szúnyogháló, alumínium, erkélyajtó'
    }

    article_file = 'conduit_test_articles.csv'


class Urls:
    home_url = 'http://localhost:1667/#/'

    user_url = 'http://localhost:1667/#/@user1test20230313%20/'

    my_fedd_url = 'http://localhost:1667/#/my-feed'

    signin_url = 'http://localhost:1667/#/login'

    signup_url = 'http://localhost:1667/#/register'

    new_article_url = 'http://localhost:1667/#/editor'

    settings_url = 'http://localhost:1667/#/settings'
