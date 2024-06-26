import uvicorn
from fastapi import Depends, FastAPI
from pkg.routes import authentication
from pkg.routes.user_registration import user_actions
from pkg.routes.customer import customer
from pkg.routes.members import members
from pkg.database.database import database
# auth
from fastapi.security import (OAuth2PasswordBearer)
# CORS headers
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS url
origins = [
   "http://localhost:3000",  # Local development frontend
    "https://rxtn.onrender.com",  # Production backend
    '*'
]

# adding middleware
app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=['*'],
                   allow_headers=['*']
                   )

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')
app.include_router(user_actions.user_router, tags=["users"])
app.include_router(members.members_router, tags=["Partners"])
app.include_router(customer.customer_router, tags=["customer"])
app.include_router(authentication.auth_router, tags=["authentication"])

@app.get("/health")
def index():
    return {"Message": "Service is Up"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8110)
