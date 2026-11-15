"""
🟡 Middleware is a way to run a piece of code for each request in FastAPI, like:
    1. "CORS"
    2. "Request timing"
    3. "Request id"
    4. "Logging"
    5. "Compression"
    6. "Trusted hosts"
    7. "Common response headers"
    8. "Global API key check"
    9. "Rate limiting"
    10. "Maintenance mode"

🟡 Things we do only using middleware are where we need to run a piece of code always for each request. We don't use middleware for:
    1. "Authentication"                 --> Use "Depends(get_current_user) instead
    2. "Role-based Access"              --> Use RoleChecker(["admin"]) instead
    3. "Pagination Values"              --> Read from query directly
    4. "Body Validation"                --> Pydantic Models
    5. "Query and Path Validation"      --> Query(), Path()
    6. "Error Handling"                 --> @app.exception_handler()
    8. "Hiding Field like Password      --> Response Model

🟡 The order of middleware is like this:
    1. The middleware added at the end will run first, then the middleware added second last, and then
       it runs the actual route if we have just two middlewares.
"""
