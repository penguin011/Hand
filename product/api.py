import csv
import json
import datetime
import requests
import uuid
import time

from multiprocessing import Process

import os

import subprocess
import sys

from django.conf import settings
from io import BytesIO
from PIL import Image
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from dry_rest_permissions.generics import DRYPermissions

from ebaysdk.trading import Connection
from .models import Product, DeletedList, OrderList
from .serializers import ProductSerializer, DeletedListSerializer
from product.scrape.engineselector import select_engine
from utils.convertcurrency import convert
from utils.ebay_policy import DISPATCHTIMEMAX, RETURN_POLICY, SHIPPING_POLICY
from utils.scrape_site import scraping_site
from utils.profit_formula import profit_formula
from .filterbackend import FilterBackend

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = (DRYPermissions, )

    @action(detail=False, methods=['POST'])
    def scrape_data(self, request):
        url = request.data['url']
        engine = select_engine(url=url)
        if engine:
            engine = engine()
            try:
                data = engine.scrape_data(source_url=url)
                # data['price_en'] = convert('JPY', 'USD', data['price_jp'])

                return Response(
                    data=data,
                    status=200
                )
            except Exception as err:
                raise err
        
        return Response(
            data='入力したサイトへのサービスはまだサポートされていません。',
            status=400
        )
            
    @action(detail=False, methods=['POST'])
    def validate_product(self, request):
        info = request.data['product_info']
        ecsite = info['ecsite_url']
        ebay = info['ebay_url']
        itemID = info['item_id']

        # validate duplicate
        # products = Product.objects.filter(purchase_url=ecsite).values | Product.objects.filter(ebay_url=ebay).values

        # if len(products) > 0:
        #     return Response(error='すでに存在しています！', status=400) 

        # Get ebay information
        # try:
            # Set up the API connection
            # api = Connection(appid=request.user.app_id, devid=request.user.dev_id, certid=request.user.cert_id, token=request.user.ebay_token, config_file=None)

            # response = api.execute(
            #     'GetItem',
            #     {
            #         'ItemID': itemID,
            #         'IncludeItemSpecifics': 'True'
            #     }
            # )

            # item_specifics = response.reply.Item.ItemSpecifics.NameValueList
            # required_specifics = []
            # optional_specifics = []
            
            # for item_specific in item_specifics:
            #     if(getattr(item_specific, 'Name') == 'Brand' or getattr(item_specific, 'Name') == 'Type'):
            #         required_specifics.append(
            #             {
            #                 'Name': item_specific.Name,
            #                 'Value': item_specific.Value,
            #                 'Condition': 'Required',
            #             }
            #         )
            #     else:
            #         optional_specifics.append(
            #             {
            #                 'Name': item_specific.Name,
            #                 'Value': item_specific.Value,
            #                 'Condition': 'Optional',
            #             }
            #         )
            # result = required_specifics + optional_specifics

        #     return Response(
        #         data=result,
        #         status=200
        #     )
        # except Exception as err:
        #     return Response({'error': 'Invalid eBay product info!'})

        # Scraping data
        engine = select_engine(url=ecsite)
        if engine:
            engine = engine()
            try:
                data = engine.scrape_data(source_url=ecsite)
                data['sell_price_en'] = convert('JPY', 'USD', data['purchase_price'])

                return Response(
                    data=data,
                    status=200
                )
            except Exception as err:
                raise err
        else:
            return Response(
                error='入力したサイトへのサービスはまだサポートされていません。', status=200
            )

        # return Response({'valid': True}, status=200)
    
    @action(detail=False, methods=['POST'])
    def get_item_specific(self, request):
        item_number = request.data['item_number']

        try:
            # Set up the API connection
            api = Connection(appid=request.user.app_id, devid=request.user.dev_id, certid=request.user.cert_id, token=request.user.ebay_token, config_file=None)
            response = api.execute(
                'GetItem',
                {
                    'ItemID': item_number,
                    'IncludeItemSpecifics': 'True'
                }
            )
            item_specifics = response.reply.Item.ItemSpecifics.NameValueList
            required_specifics = []
            optional_specifics = []
            for item_specific in item_specifics:
                if(getattr(item_specific, 'Name') == 'Brand' or getattr(item_specific, 'Name') == 'Type'):
                    required_specifics.append(
                        {
                            'Name': item_specific.Name,
                            'Value': item_specific.Value,
                            'Condition': 'Required',
                        }
                    )
                else:
                    optional_specifics.append(
                        {
                            'Name': item_specific.Name,
                            'Value': item_specific.Value,
                            'Condition': 'Optional',
                        }
                    )
            result = required_specifics + optional_specifics
            return Response(
                data=result,
                status=200
            )
        except Exception as err:
            raise err
        
    def fff():
        print('sfsdf')
        with open(file=str(settings.BASE_DIR / 'utils/1.txt'),  mode='w', encoding='utf-8') as f:
            f.write('ddddddddddd')

        return True
    
        
    @action(detail=False, methods=['GET'])
    def get_products(self, request):

        perPageNum = request.GET.get('pageSize')
        page = request.GET.get('page')
        user = request.GET.get('user')

        products_list = []

        # pid = subprocess.Popen([sys.executable, settings.BASE_DIR / "product/scraping_bot.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

        # print(pid)  

        print(1)
        # subprocess.run(["python", "product/scraping_bot.py"], stdout=subprocess.PIPE)

        # os.system('python product/scraping_bot.py')

        p = Process(target=self.fff)
        p.start()

        print(2)

        if user == '':
            products_list = Product.objects.all().order_by('id')
        else:
            products_list = Product.objects.filter(created_by=user).order_by('id')

        paginator = Paginator(products_list, perPageNum)

        try:
            products = paginator.page(page).object_list
        except PageNotAnInteger:
            products = paginator.page(1).object_list
        except EmptyPage:
            products = paginator.page(paginator.num_pages).object_list

        return Response({'count': paginator.count, 'products': products.values()}, status=200)
    
    @action(detail=False, methods=['POST'])
    def add_item(self, request):
        # Product
        item = request.data['product']

        print(item['ec_site'])

        product = ()

        try:
            product = Product(
                created_at=item['created_at'],
                product_name=item['product_name'],
                ec_site=item['ec_site'],
                purchase_url=item['purchase_url'],
                ebay_url=item['ebay_url'],
                purchase_price=item['purchase_price'],
                sell_price_en=item['sell_price_en'],
                profit=item['profit'],
                profit_rate=item['profit_rate'],
                prima=item['prima'],
                shipping=item['shipping'],
                quantity=item['quantity'],
                created_by=item['created_by'],
                notes=item['notes']
            )
            
            product.save()

            return Response(
                {'Success!'},
                status=200
            )
            
        except Exception as err:
            return Response(error='登録操作が失敗しました!', status=400)
        
    @action(detail=False, methods=['GET'])  
    def get_results(self, request):

        worker = request.GET.get('worker')
        month = request.GET.get('month')

        results = Product.objects.filter(created_by=worker, created_at__startswith=month).order_by('id').values('id', 'created_at', 'created_by')

        return Response({'results': results}, status=200)
    
        
    @action(detail=False, methods=['GET'])    
    def get_orders(self, request):

        perPageNum = request.GET.get('pageSize')
        page = request.GET.get('page')
        user = request.GET.get('user')

        orders_list = []

        if user == '':
            orders_list = OrderList.objects.all().order_by('id')
        else:
            orders_list = OrderList.objects.filter(created_by=user).order_by('id')

        paginator = Paginator(orders_list, perPageNum)

        try:
            orders = paginator.page(page).object_list
        except PageNotAnInteger:
            orders = paginator.page(1).object_list
        except EmptyPage:
            orders = paginator.page(paginator.num_pages).object_list

        return Response({'count': paginator.count, 'orders': orders.values()}, status=200)
    
    @action(detail=False, methods=['POST'])
    def add_order_item(self, request):
        # Product
        item = request.data['order']

        order = ()

        try:
            order = OrderList(
                created_at=item['created_at'],
                product_name=item['product_name'],
                ec_site=item['ec_site'],
                purchase_url=item['purchase_url'],
                ebay_url=item['ebay_url'],
                purchase_price=item['purchase_price'],
                sell_price_en=item['sell_price_en'],
                profit=item['profit'],
                profit_rate=item['profit_rate'],
                prima=item['prima'],
                shipping=item['shipping'],
                quantity=item['quantity'],
                order_num=item['order_num'],
                ordered_at=item['ordered_at'],
                created_by=item['created_by'],
                notes=item['notes']
            )
            
            order.save()

            return Response(
                {'Success!'},
                status=200
            )
            
        except Exception as err:
            return Response(error='オーダー商品登録作業が失敗しました！', status=400)

    @action(detail=False, methods=['GET'])  
    def get_deleted_items(self, request):

        perPageNum = request.GET.get('pageSize')
        page = request.GET.get('page')

        deletes_list = DeletedList.objects.all().order_by('id')

        paginator = Paginator(deletes_list, perPageNum)

        try:
            deletes = paginator.page(page).object_list
        except PageNotAnInteger:
            deletes = paginator.page(1).object_list
        except EmptyPage:
            deletes = paginator.page(paginator.num_pages).object_list

        return Response({'count': paginator.count, 'deleted_items': deletes.values()}, status=200)
    
    @action(detail=False, methods=['POST'])  
    def delelet_product(self, id):
        pid = id
        item = Product.objects.get(id=pid)

        delete_item = ()

        try:
            date = datetime.datetime.now()

            delete_item = DeletedList(
                created_at=item['created_at'],
                updated_at='',
                product_name=item['product_name'],
                ec_site=item['ec_site'],
                purchase_url=item['purchase_url'],
                ebay_url=item['ebay_url'],
                purchase_price=item['purchase_price'],
                sell_price_en=item['sell_price_en'],
                profit=item['profit'],
                prima=item['prima'],
                shipping=item['shipping'],
                quantity=item['quantity'],
                order_num=item['order_num'],
                ordered_at=item['ordered_at'],
                created_by=item['created_by'],
                notes=item['notes'],
                deleted_at=date
            )
            
            delete_item.save()
            item.delete()

            return True
        except:
            return False

        return Response(data='success!', status=200)
    
    @action(detail=False, methods=['GET'])
    def shipping_fee(self, request):
        with open(file=str(settings.BASE_DIR / 'utils/shipping_fee.txt'),  mode='r', encoding='utf-8') as f:
            fee = f.read()
        
        return Response(
            data=json.loads(fee),
            status=200
        )
    
    @action(detail=False, methods=['GET'])
    def settings_attr(self, request):
        with open(file=str(settings.BASE_DIR / 'utils/settings_attrs.txt'),  mode='r', encoding='utf-8') as f:
            settings_attrs = f.read()
        
        return Response(
            data=json.loads(settings_attrs),
            status=200
        )
    
    @action(detail=False, methods=['POST'])
    def update_settings_attr(self, request):
        settings_attr = request.data['settings_attr']
        
        with open(file=str(settings.BASE_DIR / 'utils/settings_attrs.txt'),  mode='w', encoding='utf-8') as f:
            f.write(json.dumps(settings_attr, indent=4))

        return Response(
            data=settings_attr,
            status=200
        )
    
    @action(detail=False, methods=['GET'])
    def get_ecsites(self, request):
        with open(file=str(settings.BASE_DIR / 'utils/ecsites.txt'),  mode='r', encoding='utf-8') as f:
            ecsites = f.read()
        
        return Response(
            data=json.loads(ecsites),
            status=200
        )
    
    @action(detail=False, methods=['POST'])
    def update_ecsites(self, request):
        ecsites = request.data['ecsites']
        with open(file=str(settings.BASE_DIR / 'utils/ecsites.txt'),  mode='w', encoding='utf-8') as f:
            f.write(json.dumps(ecsites, indent=4))

        return Response(
            data='Success',
            status=200
        )
    
    @action(detail=False, methods=['POST'])
    def download_product(self, request):
        with open(file=str(settings.BASE_DIR / 'media/products.csv'),  mode='w', encoding='utf-8', newline='') as f:
            fieldnames = ['商品名', 'EC site', '仕入れ URL', 'eBay URL', '利益額', '利益率', '仕入価格（円）', 'フリマ送料', '仕入合計（円）', '販売価格', '輸出送料', '出品者', '備考']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            
            for product in Product.objects.all():
                writer.writerow({
                    '商品名': product.product_name,
                    'EC site': product.ec_site, 
                    '仕入れ URL': product.purchase_url, 
                    'eBay URL': product.ebay_url, 
                    '利益額': product.profit, 
                    '利益率': product.profit_rate, 
                    '仕入価格（円）': product.purchase_price, 
                    'フリマ送料': product.prima, 
                    '仕入合計（円）': product.purchase_price + product.prima, 
                    '販売価格': product.sell_price_en, 
                    '輸出送料': product.shipping, 
                    '出品者': product.created_by, 
                    '備考': product.notes
                })
        return Response(
            data='Success',
            status=200
        )