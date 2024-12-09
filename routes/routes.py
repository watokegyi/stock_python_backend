from flask import Blueprint, request
from controllers.stock_controller import (
    
    find_products_by_product_kind,
    create_or_update_product_with_variants,
    upload_image,
    get_image,
    delete_product_kind_and_product,
    export_product_data,
    import_product_data
)

api=Blueprint('api',__name__)


api.add_url_rule("/product-types-with-products","find_products_by_product_kind",find_products_by_product_kind,methods=["GET"])
api.add_url_rule("/updateWithVariants/<id>","create_or_update_product_with_variants",create_or_update_product_with_variants,methods=["PUT"])
api.add_url_rule(
    "/imageUpload", 
    "upload_image", 
    upload_image, 
    methods=["POST"]
)

api.add_url_rule(
    "/assets/images/<filename>", 
    "get_image", 
    get_image, 
    methods=["GET"]
)
api.add_url_rule("/allproductbypK/<id>","delete_product_kind_and_product",delete_product_kind_and_product,methods=["DELETE"])

api.add_url_rule("/productdata/export","export_product_data",export_product_data,methods=["GET"])

api.add_url_rule("/productdata/import", "import_product_data", import_product_data, methods=["POST"])