# CONTROLE DE ALUGUEL

## Start Project

![start project](/assets/images/start_project.png)
Base: [Canal youtube](https://www.youtube.com/watch?v=Mgd-WfzhlUE&t=1s)

=> Projeto django encontrado no workana para controle de alugueis

## Descrição do Projeto

![Descrição do Projeto](/assets/images/project_description.png)

![Fluxograma do Projeto](/assets/images/fluxograma_projeto.png)

## Entendendo o terminal

No shell:

<!-- Importa a classe -->
In: from apps.core.models import Immobile

***

<!-- Forma de filtrar algo -->
In: x = Immobile.objects.filter(is_locate=True)

In: x
Out:
    <QuerySet [<Immobile: 784512 - APARTAMENTO>, <Immobile: 456789 - KITNET>, <Immobile: 123456 - KITNET>]>

<!------------------------------------------------->

<!-- Contar quantidade de ocorrencias -->
In: Immobile.objects.filter(is_locate=True).count()
Out:
    3

In: Immobile.objects.filter(is_locate=False).count()
Out:
    8

In: Immobile.objects.filter(type_item='KITNET').count()
Out:
    4

<!------------------------------------------------->

<!-- Mostrar as ocorrências -->
In: Immobile.objects.filter(type_item='KITNET')
Out:
    <QuerySet [<Immobile: 123456 - KITNET>, <Immobile: 235689 - KITNET>, <Immobile: 456789 - KITNET>, <Immobile: 123456 - KITNET>]>

<!------------------------------------------------->

<!-- Filtrar com mais de um parâmetro -->
In: Immobile.objects.filter(type_item='KITNET', price__gte=1000)
Out:
    <QuerySet [<Immobile: 123456 - KITNET>, <Immobile: 235689 - KITNET>, <Immobile: 456789 - KITNET>]>

Ex:
    Greater than:
        Person.objects.filter(age__gt=20)

    Greater than or equal to:
        Person.objects.filter(age__gte=20)

    Less than:
        Person.objects.filter(age__lt=20)

    Less than or equal to:
        Person.objects.filter(age__lte=20)

<!------------------------------------------------->

<!-- Importando a classe e destrinchando - a -->
In: from apps.core.models import ImmobileImages

<!-- ##### ImmobileImages ##### -->
In: x = ImmobileImages
<!-------------------------------->

In: dir(x) <!-- Propriedades existentes em 'x' -->
Out:
    [
        'DoesNotExist', 'MultipleObjectsReturned', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_check_column_name_clashes', '_check_constraints', '_check_db_table_comment', '_check_default_pk', '_check_field_name_clashes', '_check_fields', '_check_id_field', '_check_indexes', '_check_local_fields', '_check_long_column_names', '_check_m2m_through_same_relationship', '_check_managers', '_check_model', '_check_model_name_db_lookup_clashes', '_check_ordering', '_check_property_name_related_field_accessor_clashes', '_check_single_primary_key', '_check_swappable', '_check_unique_together', '_do_insert', '_do_update', '_get_FIELD_display', '_get_expr_references', '_get_field_expression_map', '_get_next_or_previous_by_FIELD', '_get_next_or_previous_in_order', '_get_pk_val', '_get_unique_checks', '_meta', '_parse_params', '_perform_date_checks', '_perform_unique_checks', '_prepare_related_fields_for_save', '_save_parents', '_save_table', '_set_pk_val', '_validate_force_insert', 'adelete', 'arefresh_from_db', 'asave', 'check', 'clean', 'clean_fields', 'date_error_message', 'delete', 'from_db', 'full_clean', 'get_constraints', 'get_deferred_fields', 'id', 'image', 'immobile', 'immobile_id', 'objects', 'pk', 'prepare_database_save', 'refresh_from_db', 'save', 'save_base', 'serializable_value', 'unique_error_message', 'validate_constraints', 'validate_unique'
    ]

In: x <!-- Instancia de x -->
Out:
    <class 'apps.core.models.ImmobileImages'>

<!-- ##### ImmobileImages.objects ##### -->
    In: x = ImmobileImages.objects
<!---------------------------------------->

In: x
Out:
    <django.db.models.manager.Manager object at 0x7428e594baa0>

In: dir(x)
Out:
    [
        '__class__', '__class_getitem__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slotnames__', '__str__', '__subclasshook__', '__weakref__', '_constructor_args', '_db', '_get_queryset_methods', '_hints', '_insert', '_queryset_class', '_set_creation_counter', '_update', 'aaggregate', 'abulk_create', 'abulk_update', 'acontains', 'acount', 'acreate', 'aearliest', 'aexists', 'aexplain', 'afirst', 'aget', 'aget_or_create', 'aggregate', 'ain_bulk', 'aiterator', 'alast', 'alatest', 'alias', 'all', 'annotate', 'aupdate', 'aupdate_or_create', 'auto_created', 'bulk_create', 'bulk_update', 'check', 'complex_filter', 'contains', 'contribute_to_class', 'count', 'create', 'creation_counter', 'dates', 'datetimes', 'db', 'db_manager', 'deconstruct', 'defer', 'difference', 'distinct', 'earliest', 'exclude', 'exists', 'explain', 'extra', 'filter', 'first', 'from_queryset', 'get', 'get_or_create', 'get_queryset', 'in_bulk', 'intersection', 'iterator', 'last', 'latest', 'model', 'name', 'none', 'only', 'order_by', 'prefetch_related', 'raw', 'reverse', 'select_for_update', 'select_related', 'union', 'update', 'update_or_create', 'use_in_migrations', 'using', 'values', 'values_list'
    ]

<!-- ##### ImmobileImages.objects.last() ##### -->
    In: x = ImmobileImages.objects.last()
<!----------------------------------------------->

In: x
Out:
    <ImmobileImages: 123456>

In: dir(x)
Out:
    [
        'DoesNotExist', 'MultipleObjectsReturned', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_check_column_name_clashes', '_check_constraints', '_check_db_table_comment', '_check_default_pk', '_check_field_name_clashes', '_check_fields', '_check_id_field', '_check_indexes', '_check_local_fields', '_check_long_column_names', '_check_m2m_through_same_relationship', '_check_managers', '_check_model', '_check_model_name_db_lookup_clashes', '_check_ordering', '_check_property_name_related_field_accessor_clashes', '_check_single_primary_key', '_check_swappable', '_check_unique_together', '_do_insert', '_do_update', '_get_FIELD_display', '_get_expr_references', '_get_field_expression_map', '_get_next_or_previous_by_FIELD', '_get_next_or_previous_in_order', '_get_pk_val', '_get_unique_checks', '_meta', '_parse_params', '_perform_date_checks', '_perform_unique_checks', '_prepare_related_fields_for_save', '_save_parents', '_save_table', '_set_pk_val', '_state', '_validate_force_insert', 'adelete', 'arefresh_from_db', 'asave', 'check', 'clean', 'clean_fields', 'date_error_message', 'delete', 'from_db', 'full_clean', 'get_constraints', 'get_deferred_fields', 'id', 'image', 'immobile', 'immobile_id', 'objects', 'pk', 'prepare_database_save', 'refresh_from_db', 'save', 'save_base', 'serializable_value', 'unique_error_message', 'validate_constraints', 'validate_unique'
    ]

In: x.image
Out:
    <ImageFieldFile: imgs/WhatsApp_Image_2023-04-12_at_19.24.25.jpeg>

In: dir(x.image)

Out:
    [
        'DEFAULT_CHUNK_SIZE', '__bool__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_committed', '_del_file', '_file', '_get_file', '_get_image_dimensions', '_require_file', '_set_file', '_set_instance_attribute', 'chunks', 'close', 'closed', 'delete', 'encoding', 'field', 'file', 'fileno', 'flush', 'height', 'instance', 'isatty', 'multiple_chunks', 'name', 'newlines', 'open', 'path', 'read', 'readable', 'readinto', 'readline', 'readlines', 'save', 'seek', 'seekable', 'size', 'storage', 'tell', 'truncate', 'url', 'width', 'writable', 'write', 'writelines'
    ]

<!-- ##### ImmobileImages.objects.last().image ##### -->
    In: x = ImmobileImages.objects.last().image
<!----------------------------------------------------->

In: dir(x)
Out:
    [
        'DEFAULT_CHUNK_SIZE', '__bool__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_committed', '_del_file', '_file', '_get_file', '_get_image_dimensions', '_require_file', '_set_file', '_set_instance_attribute', 'chunks', 'close', 'closed', 'delete', 'encoding', 'field', 'file', 'fileno', 'flush', 'height', 'instance', 'isatty', 'multiple_chunks', 'name', 'newlines', 'open', 'path', 'read', 'readable', 'readinto', 'readline', 'readlines', 'save', 'seek', 'seekable', 'size', 'storage', 'tell', 'truncate', 'url', 'width', 'writable', 'write', 'writelines'
    ]

<!-- ##### ImmobileImages.objects.last().image.path ##### -->
    In: x = ImmobileImages.objects.last().image.path
<!---------------------------------------------------------->

In: dir(x)
Out:
    [
        '__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'
    ]

In: x
Out:
    '/home/laura-carlotta/dev-projects/python-study/django_projects/workana/media/imgs/WhatsApp_Image_2023-04-12_at_19.24.25.jpeg'

In: x = ImmobileImages.objects.last().image.url
In: x
Out:
    '/media/imgs/WhatsApp_Image_2023-04-12_at_19.24.25.jpeg'

<!-- Depois da atribuição de 'x', podemos pegar infos a partir do meio -->

In: x = ImmobileImages.objects.last()
In: x.image
Out:
    <ImageFieldFile: imgs/WhatsApp_Image_2023-04-12_at_19.24.25.jpeg>

In: x.image.path
Out:
    '/home/laura-carlotta/dev-projects/python-study/django_projects/workana/media/imgs/WhatsApp_Image_2023-04-12_at_19.24.25.jpeg'

In: x.image.url
Out:
    '/media/imgs/WhatsApp_Image_2023-04-12_at_19.24.25.jpeg'

In: x.immobile
Out:
    <Immobile: 123456 - KITNET>

<!-- Ao invés de colocar a variável a função 'dir()', ao final podemos atribuir o -->
<!-- .__dir__ que assim irá demostrar só aquilo que construimos na classe -->

In: x.immobile.__dict__
Out:
    {'_state': <django.db.models.base.ModelState object at 0x7428e59a0590>, 'id': 11, 'code': '123456', 'type_item': 'KITNET', 'address': 'tgerst', 'price': Decimal('22222.00'), 'is_locate': False}

<!-- Podemos atribuir ao .objects o atributo .all(), ele retornará um querySet, que é um retorno do banco com todos os valores criados a partir daquela classe. -->

In: from apps.core.models import Immobile
In: Immobile.objects.all()
Out:
    <QuerySet [<Immobile: 123456 - KITNET>, <Immobile: 7896 - APARTAMENTO>, <Immobile: 258369 - HOUSE>, <Immobile: 147258 - HOUSE>, <Immobile: 784512 - APARTAMENTO>, <Immobile: 235689 - KITNET>, <Immobile: 124578 - APARTAMENTO>, <Immobile: 456789 - KITNET>, <Immobile: 123456 - KITNET>, <Immobile: 789456 - APARTAMENTO>, <Immobile: 034547 - APARTAMENTO>]>

<!-- O pprint, é uma forma de apresentação desses retornos de forma identada (mais legível) -->
<!-------------------------------------------------------------------------------------------->

In: from pprint import pprint
In: x = ImmobileImages.objects.last()

In: pprint(dir(x))
Out:
    [
        'DoesNotExist',
        'MultipleObjectsReturned',
        '__class__',
        '__delattr__',
        '__dict__',
        '__dir__',
        '__doc__',
        '__eq__',
        '__format__',
        '__ge__',
        '__getattribute__',
        '__getstate__',
        '__gt__',
        '__hash__',
        '__init__',
        '__init_subclass__',
        '__le__',
        '__lt__',
        '__module__',
        '__ne__',
        '__new__',
        '__reduce__',
        '__reduce_ex__',
        '__repr__',
        '__setattr__',
        '__setstate__',
        '__sizeof__',
        '__str__',
        '__subclasshook__',
        '__weakref__',
        '_check_column_name_clashes',
        '_check_constraints',
        '_check_db_table_comment',
        '_check_default_pk',
        '_check_field_name_clashes',
        '_check_fields',
        '_check_id_field',
        '_check_indexes',
        '_check_local_fields',
        '_check_long_column_names',
        '_check_m2m_through_same_relationship',
        '_check_managers',
        '_check_model',
        '_check_model_name_db_lookup_clashes',
        '_check_ordering',
        '_check_property_name_related_field_accessor_clashes',
        '_check_single_primary_key',
        '_check_swappable',
        '_check_unique_together',
        '_do_insert',
        '_do_update',
        '_get_FIELD_display',
        '_get_expr_references',
        '_get_field_expression_map',
        '_get_next_or_previous_by_FIELD',
        '_get_next_or_previous_in_order',
        '_get_pk_val',
        '_get_unique_checks',
        '_meta',
        '_parse_params',
        '_perform_date_checks',
        '_perform_unique_checks',
        '_prepare_related_fields_for_save',
        '_save_parents',
        '_save_table',
        '_set_pk_val',
        '_state',
        '_validate_force_insert',
        'adelete',
        'arefresh_from_db',
        'asave',
        'check',
        'clean',
        'clean_fields',
        'date_error_message',
        'delete',
        'from_db',
        'full_clean',
        'get_constraints',
        'get_deferred_fields',
        'id',
        'image',
        'immobile',
        'immobile_id',
        'objects',
        'pk',
        'prepare_database_save',
        'refresh_from_db',
        'save',
        'save_base',
        'serializable_value',
        'unique_error_message',
        'validate_constraints',
        'validate_unique'
    ]
