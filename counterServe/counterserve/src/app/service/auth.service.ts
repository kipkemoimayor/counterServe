import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private authApi: string = environment.apiAuth;

  constructor(private http: HttpClient) { }

  /**
   * creates an auth token on login
   * @param loginParams username and password
   * @returns auth token
   */
  loginUser(loginParams: any): Observable<any> {
    return <any>this.http.post(this.authApi, loginParams)
  }

  saveUserToLocalStorage(user: any) {
    localStorage.setItem('axuserIxaver', JSON.stringify(user));
  }

  getCurrentUser(): any {
    return JSON.parse(localStorage.getItem('axuserIxaver'));
  }

  //logout user
  logoutUser() {
    localStorage.clear();
  }

  isAuthenticated(): Promise<boolean> {
    return new Promise((resolve, reject) => {
      if (this.getCurrentUser().authToken){
        resolve(this.getCurrentUser())
      }else{
        reject(null)
      }
    })
  }


}
