export interface Iuser {
    username: string;
    email: string;
    password: string;
    c_password: string;
}

export interface ILoginuser {
    username: string;
    password: string;
}

export interface Iresult {
    count: number;
    results: any[];
    prev: number;
    next: number;
}

export interface Ipost {
    title: string;
    description: string;
    content: string;
    id?: number;
    // pub_date:string;
}

