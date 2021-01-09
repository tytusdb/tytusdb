export class Product {
    
    ID_PRODUCTO: number;
    PRODUCTO: string;
    IMAGEN: string;
    DESCRIPCION :  string;
    PRECIO : number;
    FECHA_POST : string;
    CANTIDAD_DISPONIBLE : number;
    USUARIO_ID_USUARIO : number;

}

export class ProductCat {
    
    ID_PRODUCTO: number;
    PRODUCTO: string;
    IMAGEN: string;
    DESCRIPCION :  string;
    PRECIO : number;
    FECHA_POST : string;
    CANTIDAD_DISPONIBLE : number;
    USUARIO_ID_USUARIO : number;
    CATEGORIA : [];
}