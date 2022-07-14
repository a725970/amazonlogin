from audible.auth import Authenticator



if __name__ == "__main__":
    password ="Cc112211"
    user="6061110@gmail.com"
    myproxy="http://127.0.0.1:7890"
    auth = Authenticator.from_login(
        username=user,
        proxys=myproxy,
        password=password,
        locale="us"
    )

    print(auth.website_cookies)
    print("end")

