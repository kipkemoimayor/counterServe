import { HTTP_INTERCEPTORS } from '@angular/common/http';
import { ApiAuthInterceptor } from './api-key.interceptor';

export const httpInterceptorProviders = [
    { provide: HTTP_INTERCEPTORS, useClass: ApiAuthInterceptor, multi: true }
]