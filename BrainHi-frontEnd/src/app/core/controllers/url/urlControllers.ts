export const UrlControllers = {
    Urlbase:"http://20.72.171.198/Api",
    Authentication: {
        Name: 'Authentication',
        Methods: {
            LogIn: 'Authentication/LogIn',
            SignInUsingToken: 'Authentication/SignInUsingToken',
            LogOut: 'Authentication/LogOut',
            RegisterUser:'Authentication/RegisterUser'
        },
    },
    User: {
        Name: 'User',
        Methods: {
            Register:'User/Register'
        },
    },

    Patient: {
        Name: 'Patient',
        Methods: {
            Register:'Patient/Register'
        },
    },
}
