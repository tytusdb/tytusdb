export class UserLogin {
    ID_USUARIO: number;
    PASSWORD?: string;
    NOMBRE: string;
    APELLIDOS: string;
    EMAIL: string;
    ROL_ID_ROL: String;
    constructor(object: any)
    {
        this.ID_USUARIO = (object.ID_USUARIO) ? object.ID_USUARIO : null;
        this.PASSWORD = (object.PASSWORD) ? object.PASSWORD : null;
        this.NOMBRE = (object.NOMBRE) ? object.NOMBRE : null;
        this.APELLIDOS = (object.APELLIDOS) ? object.APELLIDOS : null;
    }
}