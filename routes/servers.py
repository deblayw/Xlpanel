# type: ignore
from __main__ import *
import time

@app.route("/servers/", methods=["GET"])
def servers():
    if request.method == "GET":
        beginT = time.time()
        check = helper.chSID(request.cookies.get("sid"))
        if (not check[0]):
            return redirect("/login")

        uSv = helper.listPteroServer(check[1]["user"])
        uDt = helper.checkPteroUser(check[1]["user"])
        if (uSv[0] == False) or (uDt[0] == False):
            return f"""Something went wrong!\n\nuSv response:\n{uSv}\n\nuDt response:\n{uDt}"""

        return render_template(
            "server.html",
            name=name,
            isAdmin=uDt[1].get("root_admin",False),
            user=check[1]["user"],
            sv = uSv[1],
            mIt=menuItems,
            coin=check[1]["coin"],
            loadTime=int((time.time()-beginT)*100000)/100000
        )