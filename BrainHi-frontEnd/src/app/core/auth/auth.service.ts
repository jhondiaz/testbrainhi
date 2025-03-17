import { HttpClient, HttpParams } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';
import { AuthUtils } from 'app/core/auth/auth.utils';
import { UserService } from 'app/core/user/user.service';
import { catchError, Observable, of, switchMap, throwError } from 'rxjs';
import { UrlControllers } from '../controllers/url/urlControllers';
import { User } from '../user/user.types';

@Injectable({ providedIn: 'root' })
export class AuthService {
    private _authenticated: boolean = false;
    private _httpClient = inject(HttpClient);
    private _userService = inject(UserService);
    private urlBase: string;

    // -----------------------------------------------------------------------------------------------------
    // @ Accessors
    // -----------------------------------------------------------------------------------------------------

    /**
     * Setter & getter for access token
     */
    set accessToken(token: string) {
        localStorage.setItem('accessToken', token);
    }

    get accessToken(): string {
        return localStorage.getItem('accessToken') ?? '';
    }

    // -----------------------------------------------------------------------------------------------------
    // @ Public methods
    // -----------------------------------------------------------------------------------------------------

    /**
     * Forgot password
     *
     * @param email
     */
    forgotPassword(email: string): Observable<any> {
        return this._httpClient.post('api/auth/forgot-password', email);
    }

    /**
     * Reset password
     *
     * @param password
     */
    resetPassword(password: string): Observable<any> {
        return this._httpClient.post('api/auth/reset-password', password);
    }

    /**
     * Sign in
     *
     * @param credentials
     */
    signIn(credentials: { email: string; password: string }): Observable<any> {
        // Throw error, if the user is already logged in
        if (this._authenticated) {
            return throwError('User is already logged in.');
        }
        this.urlBase = UrlControllers.Urlbase;

        return this._httpClient.post(`${this.urlBase}/${UrlControllers.Authentication.Methods.LogIn}`, credentials).pipe(
            switchMap((response: any) => {
                   console.log(response)
                if (response.Codigo === 0) {
                    const { Value } = response;
                    this.accessToken = Value.token;
                    this._authenticated = true;

                    var _user:User={
                        id: Value.user.id,
                        name:Value.user.firstName+' '+ Value.user.lastName,
                        email: Value.user.email,
                        status:'online',
                        avatar:'johndiaz.png'
                    };
                    // id: string;
                    // name: string;
                    // email: string;
                    // avatar?: string;
                    // status?: string;
                    this._userService.user =_user;

                } else {
                    this._authenticated = false;
                    localStorage.clear();
                    return throwError(() => 'User is already logged in.');
                }
                return of(response);
            })
        );
    }

    /**
     * Sign in using the access token
     */
    signInUsingToken(): Observable<any> {
        this.urlBase = UrlControllers.Urlbase;

        return this._httpClient
            .get(
                `${this.urlBase}/${UrlControllers.Authentication.Methods.SignInUsingToken}`,
                {
                    params:{
                         token: this.accessToken,
                    }

                })
            .pipe(
                catchError(() =>
                    // Return false
                    of(false)
                ),
                switchMap((response: any) => {

                    if (response.codigo === 0) {
                     //   const { value } = response;
                     //   this.accessToken = value.token;
                        this._authenticated = true;
                        return of(true);
                    } else {
                        this._authenticated = false;
                        localStorage.clear();
                    }

                    // Return true
                    return of(true);
                })
            );
    }

    /**
     * Sign out
     */
    signOut(): Observable<any> {
        // Remove the access token from the local storage
        localStorage.removeItem('accessToken');

        // Set the authenticated flag to false
        this._authenticated = false;

        // Return the observable
        return of(true);
    }

    /**
     * Sign up
     *
     * @param user
     */
    signUp(user: {
        id?:string;
        firstName: string;
        lastName: string;
        phone: string;
        email: string;
        password: string;
        createDate?:string;
    }): Observable<any> {
        this.urlBase = UrlControllers.Urlbase;
        user.createDate= new Date().toDateString();
        user.id='';
        return this._httpClient.post(`${this.urlBase}/${UrlControllers.User.Methods.Register}`, user);
    }

    /**
     * Unlock session
     *
     * @param credentials
     */
    unlockSession(credentials: {
        email: string;
        password: string;
    }): Observable<any> {
        return this._httpClient.post('api/auth/unlock-session', credentials);
    }

    /**
     * Check the authentication status
     */
    check(): Observable<boolean> {
        // Check if the user is logged in
        if (this._authenticated) {
            return of(true);
        }

        // Check the access token availability
        if (!this.accessToken) {
            return of(false);
        }

        // Check the access token expire date
        if (AuthUtils.isTokenExpired(this.accessToken)) {
            return of(false);
        }

        // If the access token exists, and it didn't expire, sign in using it
        return of(true);
    }


    registerPatient(patient:any): Observable<any> {
        this.urlBase = UrlControllers.Urlbase;
        return this._httpClient.post(`${this.urlBase}/${UrlControllers.Patient.Methods.Register}`, patient);
    }


}
