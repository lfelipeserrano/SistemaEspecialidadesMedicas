PGDMP                         w            SistemaEspecialidadesMedicas    11.2    11.2 ~    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                       false            �           1262    16393    SistemaEspecialidadesMedicas    DATABASE     �   CREATE DATABASE "SistemaEspecialidadesMedicas" WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'English_United States.1252' LC_CTYPE = 'English_United States.1252';
 .   DROP DATABASE "SistemaEspecialidadesMedicas";
             DSI    false            �            1259    16785    CEM_consulta    TABLE     �  CREATE TABLE public."CEM_consulta" (
    "idConsulta" integer NOT NULL,
    "fechaConsulta" date NOT NULL,
    "pesoConsulta" integer,
    "presionConsulta" character varying(10),
    temperatura integer,
    pulso integer,
    "alturaConsulta" integer,
    observaciones text NOT NULL,
    recetas text,
    "examenesSolicitados" text,
    expediente_id integer NOT NULL,
    "idDoctor_id" integer NOT NULL
);
 "   DROP TABLE public."CEM_consulta";
       public         DSI    false            �            1259    16783    CEM_consulta_idConsulta_seq    SEQUENCE     �   CREATE SEQUENCE public."CEM_consulta_idConsulta_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public."CEM_consulta_idConsulta_seq";
       public       DSI    false    216            �           0    0    CEM_consulta_idConsulta_seq    SEQUENCE OWNED BY     a   ALTER SEQUENCE public."CEM_consulta_idConsulta_seq" OWNED BY public."CEM_consulta"."idConsulta";
            public       DSI    false    215            �            1259    16796 
   CEM_doctor    TABLE     �  CREATE TABLE public."CEM_doctor" (
    "idDoctor" integer NOT NULL,
    "primerNombreDoctor" character varying(50) NOT NULL,
    "segundoNombreDoctor" character varying(50) NOT NULL,
    "primerApellidoDoctor" character varying(50) NOT NULL,
    "segundoApellidoDoctor" character varying(50) NOT NULL,
    especialidad character varying(50) NOT NULL,
    "sexoDoctor" boolean NOT NULL,
    "fechaNacimientoDoctor" date NOT NULL,
    "telefonoDoctor" character varying(9) NOT NULL,
    "correoElectronico" character varying(50) NOT NULL,
    "duiDoctor" character varying(12) NOT NULL,
    "fotografiaDoctor" character varying(100) NOT NULL
);
     DROP TABLE public."CEM_doctor";
       public         DSI    false            �            1259    16794    CEM_doctor_idDoctor_seq    SEQUENCE     �   CREATE SEQUENCE public."CEM_doctor_idDoctor_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 0   DROP SEQUENCE public."CEM_doctor_idDoctor_seq";
       public       DSI    false    218            �           0    0    CEM_doctor_idDoctor_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public."CEM_doctor_idDoctor_seq" OWNED BY public."CEM_doctor"."idDoctor";
            public       DSI    false    217            �            1259    16804    CEM_paciente    TABLE       CREATE TABLE public."CEM_paciente" (
    id integer NOT NULL,
    expediente character varying(20) NOT NULL,
    "primerNombrePaciente" character varying(50) NOT NULL,
    "segundoNombrePaciente" character varying(50) NOT NULL,
    "primerApellidoPaciente" character varying(50) NOT NULL,
    "segundoApellidoPaciente" character varying(50) NOT NULL,
    "sexoPaciente" boolean NOT NULL,
    "fechaNacimientoPaciente" date NOT NULL,
    "alturaPaciente" integer NOT NULL,
    "pesoPaciente" double precision NOT NULL,
    "telefonoPaciente" character varying(9) NOT NULL,
    "fotografiaPaciente" character varying(100) NOT NULL,
    institucion character varying(50) NOT NULL,
    alergias text NOT NULL,
    antecedentes text NOT NULL,
    "idDoctor_id" integer NOT NULL
);
 "   DROP TABLE public."CEM_paciente";
       public         DSI    false            �            1259    16802    CEM_paciente_id_seq    SEQUENCE     �   CREATE SEQUENCE public."CEM_paciente_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public."CEM_paciente_id_seq";
       public       DSI    false    220            �           0    0    CEM_paciente_id_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE public."CEM_paciente_id_seq" OWNED BY public."CEM_paciente".id;
            public       DSI    false    219            �            1259    16426 
   auth_group    TABLE     e   CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);
    DROP TABLE public.auth_group;
       public         DSI    false            �            1259    16424    auth_group_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.auth_group_id_seq;
       public       DSI    false    203            �           0    0    auth_group_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;
            public       DSI    false    202            �            1259    16436    auth_group_permissions    TABLE     �   CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);
 *   DROP TABLE public.auth_group_permissions;
       public         DSI    false            �            1259    16434    auth_group_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.auth_group_permissions_id_seq;
       public       DSI    false    205            �           0    0    auth_group_permissions_id_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;
            public       DSI    false    204            �            1259    16418    auth_permission    TABLE     �   CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);
 #   DROP TABLE public.auth_permission;
       public         DSI    false            �            1259    16416    auth_permission_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.auth_permission_id_seq;
       public       DSI    false    201            �           0    0    auth_permission_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;
            public       DSI    false    200            �            1259    16444 	   auth_user    TABLE     �  CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);
    DROP TABLE public.auth_user;
       public         DSI    false            �            1259    16454    auth_user_groups    TABLE        CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);
 $   DROP TABLE public.auth_user_groups;
       public         DSI    false            �            1259    16452    auth_user_groups_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_user_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.auth_user_groups_id_seq;
       public       DSI    false    209            �           0    0    auth_user_groups_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;
            public       DSI    false    208            �            1259    16442    auth_user_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.auth_user_id_seq;
       public       DSI    false    207            �           0    0    auth_user_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;
            public       DSI    false    206            �            1259    16462    auth_user_user_permissions    TABLE     �   CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);
 .   DROP TABLE public.auth_user_user_permissions;
       public         DSI    false            �            1259    16460 !   auth_user_user_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public.auth_user_user_permissions_id_seq;
       public       DSI    false    211            �           0    0 !   auth_user_user_permissions_id_seq    SEQUENCE OWNED BY     g   ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;
            public       DSI    false    210            �            1259    16522    django_admin_log    TABLE     �  CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);
 $   DROP TABLE public.django_admin_log;
       public         DSI    false            �            1259    16520    django_admin_log_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.django_admin_log_id_seq;
       public       DSI    false    213            �           0    0    django_admin_log_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;
            public       DSI    false    212            �            1259    16408    django_content_type    TABLE     �   CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);
 '   DROP TABLE public.django_content_type;
       public         DSI    false            �            1259    16406    django_content_type_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.django_content_type_id_seq;
       public       DSI    false    199            �           0    0    django_content_type_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;
            public       DSI    false    198            �            1259    16397    django_migrations    TABLE     �   CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);
 %   DROP TABLE public.django_migrations;
       public         DSI    false            �            1259    16395    django_migrations_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.django_migrations_id_seq;
       public       DSI    false    197            �           0    0    django_migrations_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;
            public       DSI    false    196            �            1259    16550    django_session    TABLE     �   CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);
 "   DROP TABLE public.django_session;
       public         DSI    false            �
           2604    16788    CEM_consulta idConsulta    DEFAULT     �   ALTER TABLE ONLY public."CEM_consulta" ALTER COLUMN "idConsulta" SET DEFAULT nextval('public."CEM_consulta_idConsulta_seq"'::regclass);
 J   ALTER TABLE public."CEM_consulta" ALTER COLUMN "idConsulta" DROP DEFAULT;
       public       DSI    false    216    215    216            �
           2604    16799    CEM_doctor idDoctor    DEFAULT     �   ALTER TABLE ONLY public."CEM_doctor" ALTER COLUMN "idDoctor" SET DEFAULT nextval('public."CEM_doctor_idDoctor_seq"'::regclass);
 F   ALTER TABLE public."CEM_doctor" ALTER COLUMN "idDoctor" DROP DEFAULT;
       public       DSI    false    217    218    218            �
           2604    16807    CEM_paciente id    DEFAULT     v   ALTER TABLE ONLY public."CEM_paciente" ALTER COLUMN id SET DEFAULT nextval('public."CEM_paciente_id_seq"'::regclass);
 @   ALTER TABLE public."CEM_paciente" ALTER COLUMN id DROP DEFAULT;
       public       DSI    false    220    219    220            �
           2604    16429    auth_group id    DEFAULT     n   ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);
 <   ALTER TABLE public.auth_group ALTER COLUMN id DROP DEFAULT;
       public       DSI    false    203    202    203            �
           2604    16439    auth_group_permissions id    DEFAULT     �   ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);
 H   ALTER TABLE public.auth_group_permissions ALTER COLUMN id DROP DEFAULT;
       public       DSI    false    204    205    205            �
           2604    16421    auth_permission id    DEFAULT     x   ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);
 A   ALTER TABLE public.auth_permission ALTER COLUMN id DROP DEFAULT;
       public       DSI    false    201    200    201            �
           2604    16447    auth_user id    DEFAULT     l   ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);
 ;   ALTER TABLE public.auth_user ALTER COLUMN id DROP DEFAULT;
       public       DSI    false    207    206    207            �
           2604    16457    auth_user_groups id    DEFAULT     z   ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);
 B   ALTER TABLE public.auth_user_groups ALTER COLUMN id DROP DEFAULT;
       public       DSI    false    208    209    209            �
           2604    16465    auth_user_user_permissions id    DEFAULT     �   ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);
 L   ALTER TABLE public.auth_user_user_permissions ALTER COLUMN id DROP DEFAULT;
       public       DSI    false    211    210    211            �
           2604    16525    django_admin_log id    DEFAULT     z   ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);
 B   ALTER TABLE public.django_admin_log ALTER COLUMN id DROP DEFAULT;
       public       DSI    false    213    212    213            �
           2604    16411    django_content_type id    DEFAULT     �   ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);
 E   ALTER TABLE public.django_content_type ALTER COLUMN id DROP DEFAULT;
       public       DSI    false    199    198    199            �
           2604    16400    django_migrations id    DEFAULT     |   ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);
 C   ALTER TABLE public.django_migrations ALTER COLUMN id DROP DEFAULT;
       public       DSI    false    197    196    197            �          0    16785    CEM_consulta 
   TABLE DATA               �   COPY public."CEM_consulta" ("idConsulta", "fechaConsulta", "pesoConsulta", "presionConsulta", temperatura, pulso, "alturaConsulta", observaciones, recetas, "examenesSolicitados", expediente_id, "idDoctor_id") FROM stdin;
    public       DSI    false    216   ը       �          0    16796 
   CEM_doctor 
   TABLE DATA                 COPY public."CEM_doctor" ("idDoctor", "primerNombreDoctor", "segundoNombreDoctor", "primerApellidoDoctor", "segundoApellidoDoctor", especialidad, "sexoDoctor", "fechaNacimientoDoctor", "telefonoDoctor", "correoElectronico", "duiDoctor", "fotografiaDoctor") FROM stdin;
    public       DSI    false    218   A�       �          0    16804    CEM_paciente 
   TABLE DATA               I  COPY public."CEM_paciente" (id, expediente, "primerNombrePaciente", "segundoNombrePaciente", "primerApellidoPaciente", "segundoApellidoPaciente", "sexoPaciente", "fechaNacimientoPaciente", "alturaPaciente", "pesoPaciente", "telefonoPaciente", "fotografiaPaciente", institucion, alergias, antecedentes, "idDoctor_id") FROM stdin;
    public       DSI    false    220   ө       �          0    16426 
   auth_group 
   TABLE DATA               .   COPY public.auth_group (id, name) FROM stdin;
    public       DSI    false    203   i�       �          0    16436    auth_group_permissions 
   TABLE DATA               M   COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
    public       DSI    false    205   ��       �          0    16418    auth_permission 
   TABLE DATA               N   COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
    public       DSI    false    201   ��       �          0    16444 	   auth_user 
   TABLE DATA               �   COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
    public       DSI    false    207   #�       �          0    16454    auth_user_groups 
   TABLE DATA               A   COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
    public       DSI    false    209   լ       �          0    16462    auth_user_user_permissions 
   TABLE DATA               P   COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
    public       DSI    false    211   �       �          0    16522    django_admin_log 
   TABLE DATA               �   COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
    public       DSI    false    213   �       �          0    16408    django_content_type 
   TABLE DATA               C   COPY public.django_content_type (id, app_label, model) FROM stdin;
    public       DSI    false    199   ��       �          0    16397    django_migrations 
   TABLE DATA               C   COPY public.django_migrations (id, app, name, applied) FROM stdin;
    public       DSI    false    197   0�       �          0    16550    django_session 
   TABLE DATA               P   COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
    public       DSI    false    214   �       �           0    0    CEM_consulta_idConsulta_seq    SEQUENCE SET     K   SELECT pg_catalog.setval('public."CEM_consulta_idConsulta_seq"', 6, true);
            public       DSI    false    215            �           0    0    CEM_doctor_idDoctor_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public."CEM_doctor_idDoctor_seq"', 2, true);
            public       DSI    false    217            �           0    0    CEM_paciente_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public."CEM_paciente_id_seq"', 1, true);
            public       DSI    false    219            �           0    0    auth_group_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);
            public       DSI    false    202            �           0    0    auth_group_permissions_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);
            public       DSI    false    204            �           0    0    auth_permission_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.auth_permission_id_seq', 36, true);
            public       DSI    false    200            �           0    0    auth_user_groups_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);
            public       DSI    false    208            �           0    0    auth_user_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.auth_user_id_seq', 1, true);
            public       DSI    false    206            �           0    0 !   auth_user_user_permissions_id_seq    SEQUENCE SET     P   SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);
            public       DSI    false    210            �           0    0    django_admin_log_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.django_admin_log_id_seq', 3, true);
            public       DSI    false    212            �           0    0    django_content_type_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.django_content_type_id_seq', 9, true);
            public       DSI    false    198            �           0    0    django_migrations_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.django_migrations_id_seq', 17, true);
            public       DSI    false    196                       2606    16793    CEM_consulta CEM_consulta_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public."CEM_consulta"
    ADD CONSTRAINT "CEM_consulta_pkey" PRIMARY KEY ("idConsulta");
 L   ALTER TABLE ONLY public."CEM_consulta" DROP CONSTRAINT "CEM_consulta_pkey";
       public         DSI    false    216            
           2606    16801    CEM_doctor CEM_doctor_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public."CEM_doctor"
    ADD CONSTRAINT "CEM_doctor_pkey" PRIMARY KEY ("idDoctor");
 H   ALTER TABLE ONLY public."CEM_doctor" DROP CONSTRAINT "CEM_doctor_pkey";
       public         DSI    false    218                       2606    16812    CEM_paciente CEM_paciente_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public."CEM_paciente"
    ADD CONSTRAINT "CEM_paciente_pkey" PRIMARY KEY (id);
 L   ALTER TABLE ONLY public."CEM_paciente" DROP CONSTRAINT "CEM_paciente_pkey";
       public         DSI    false    220            �
           2606    16433    auth_group auth_group_name_key 
   CONSTRAINT     Y   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);
 H   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_name_key;
       public         DSI    false    203            �
           2606    16488 R   auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);
 |   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq;
       public         DSI    false    205    205            �
           2606    16441 2   auth_group_permissions auth_group_permissions_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);
 \   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_pkey;
       public         DSI    false    205            �
           2606    16431    auth_group auth_group_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_pkey;
       public         DSI    false    203            �
           2606    16474 F   auth_permission auth_permission_content_type_id_codename_01ab375a_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);
 p   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq;
       public         DSI    false    201    201            �
           2606    16423 $   auth_permission auth_permission_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_pkey;
       public         DSI    false    201            �
           2606    16459 &   auth_user_groups auth_user_groups_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_pkey;
       public         DSI    false    209            �
           2606    16503 @   auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);
 j   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq;
       public         DSI    false    209    209            �
           2606    16449    auth_user auth_user_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_pkey;
       public         DSI    false    207            �
           2606    16467 :   auth_user_user_permissions auth_user_user_permissions_pkey 
   CONSTRAINT     x   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);
 d   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_pkey;
       public         DSI    false    211            �
           2606    16517 Y   auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);
 �   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq;
       public         DSI    false    211    211            �
           2606    16545     auth_user auth_user_username_key 
   CONSTRAINT     _   ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);
 J   ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_username_key;
       public         DSI    false    207            �
           2606    16531 &   django_admin_log django_admin_log_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_pkey;
       public         DSI    false    213            �
           2606    16415 E   django_content_type django_content_type_app_label_model_76bd3d3b_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);
 o   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq;
       public         DSI    false    199    199            �
           2606    16413 ,   django_content_type django_content_type_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_pkey;
       public         DSI    false    199            �
           2606    16405 (   django_migrations django_migrations_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.django_migrations DROP CONSTRAINT django_migrations_pkey;
       public         DSI    false    197                       2606    16557 "   django_session django_session_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);
 L   ALTER TABLE ONLY public.django_session DROP CONSTRAINT django_session_pkey;
       public         DSI    false    214                       1259    16819 #   CEM_consulta_expediente_id_f9aa3bf2    INDEX     i   CREATE INDEX "CEM_consulta_expediente_id_f9aa3bf2" ON public."CEM_consulta" USING btree (expediente_id);
 9   DROP INDEX public."CEM_consulta_expediente_id_f9aa3bf2";
       public         DSI    false    216                       1259    16825 !   CEM_consulta_idDoctor_id_00176ffe    INDEX     g   CREATE INDEX "CEM_consulta_idDoctor_id_00176ffe" ON public."CEM_consulta" USING btree ("idDoctor_id");
 7   DROP INDEX public."CEM_consulta_idDoctor_id_00176ffe";
       public         DSI    false    216                       1259    16818 !   CEM_paciente_idDoctor_id_90b92cdb    INDEX     g   CREATE INDEX "CEM_paciente_idDoctor_id_90b92cdb" ON public."CEM_paciente" USING btree ("idDoctor_id");
 7   DROP INDEX public."CEM_paciente_idDoctor_id_90b92cdb";
       public         DSI    false    220            �
           1259    16476    auth_group_name_a6ea08ec_like    INDEX     h   CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);
 1   DROP INDEX public.auth_group_name_a6ea08ec_like;
       public         DSI    false    203            �
           1259    16489 (   auth_group_permissions_group_id_b120cbf9    INDEX     o   CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);
 <   DROP INDEX public.auth_group_permissions_group_id_b120cbf9;
       public         DSI    false    205            �
           1259    16490 -   auth_group_permissions_permission_id_84c5c92e    INDEX     y   CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);
 A   DROP INDEX public.auth_group_permissions_permission_id_84c5c92e;
       public         DSI    false    205            �
           1259    16475 (   auth_permission_content_type_id_2f476e4b    INDEX     o   CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);
 <   DROP INDEX public.auth_permission_content_type_id_2f476e4b;
       public         DSI    false    201            �
           1259    16505 "   auth_user_groups_group_id_97559544    INDEX     c   CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);
 6   DROP INDEX public.auth_user_groups_group_id_97559544;
       public         DSI    false    209            �
           1259    16504 !   auth_user_groups_user_id_6a12ed8b    INDEX     a   CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);
 5   DROP INDEX public.auth_user_groups_user_id_6a12ed8b;
       public         DSI    false    209            �
           1259    16519 1   auth_user_user_permissions_permission_id_1fbb5f2c    INDEX     �   CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);
 E   DROP INDEX public.auth_user_user_permissions_permission_id_1fbb5f2c;
       public         DSI    false    211            �
           1259    16518 +   auth_user_user_permissions_user_id_a95ead1b    INDEX     u   CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);
 ?   DROP INDEX public.auth_user_user_permissions_user_id_a95ead1b;
       public         DSI    false    211            �
           1259    16546     auth_user_username_6821ab7c_like    INDEX     n   CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);
 4   DROP INDEX public.auth_user_username_6821ab7c_like;
       public         DSI    false    207            �
           1259    16542 )   django_admin_log_content_type_id_c4bce8eb    INDEX     q   CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);
 =   DROP INDEX public.django_admin_log_content_type_id_c4bce8eb;
       public         DSI    false    213                        1259    16543 !   django_admin_log_user_id_c564eba6    INDEX     a   CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);
 5   DROP INDEX public.django_admin_log_user_id_c564eba6;
       public         DSI    false    213                       1259    16559 #   django_session_expire_date_a5c62663    INDEX     e   CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);
 7   DROP INDEX public.django_session_expire_date_a5c62663;
       public         DSI    false    214                       1259    16558 (   django_session_session_key_c0390e0f_like    INDEX     ~   CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);
 <   DROP INDEX public.django_session_session_key_c0390e0f_like;
       public         DSI    false    214                       2606    16820 C   CEM_consulta CEM_consulta_expediente_id_f9aa3bf2_fk_CEM_paciente_id    FK CONSTRAINT     �   ALTER TABLE ONLY public."CEM_consulta"
    ADD CONSTRAINT "CEM_consulta_expediente_id_f9aa3bf2_fk_CEM_paciente_id" FOREIGN KEY (expediente_id) REFERENCES public."CEM_paciente"(id) DEFERRABLE INITIALLY DEFERRED;
 q   ALTER TABLE ONLY public."CEM_consulta" DROP CONSTRAINT "CEM_consulta_expediente_id_f9aa3bf2_fk_CEM_paciente_id";
       public       DSI    false    2829    220    216                       2606    16826 E   CEM_consulta CEM_consulta_idDoctor_id_00176ffe_fk_CEM_doctor_idDoctor    FK CONSTRAINT     �   ALTER TABLE ONLY public."CEM_consulta"
    ADD CONSTRAINT "CEM_consulta_idDoctor_id_00176ffe_fk_CEM_doctor_idDoctor" FOREIGN KEY ("idDoctor_id") REFERENCES public."CEM_doctor"("idDoctor") DEFERRABLE INITIALLY DEFERRED;
 s   ALTER TABLE ONLY public."CEM_consulta" DROP CONSTRAINT "CEM_consulta_idDoctor_id_00176ffe_fk_CEM_doctor_idDoctor";
       public       DSI    false    2826    218    216                       2606    16813 E   CEM_paciente CEM_paciente_idDoctor_id_90b92cdb_fk_CEM_doctor_idDoctor    FK CONSTRAINT     �   ALTER TABLE ONLY public."CEM_paciente"
    ADD CONSTRAINT "CEM_paciente_idDoctor_id_90b92cdb_fk_CEM_doctor_idDoctor" FOREIGN KEY ("idDoctor_id") REFERENCES public."CEM_doctor"("idDoctor") DEFERRABLE INITIALLY DEFERRED;
 s   ALTER TABLE ONLY public."CEM_paciente" DROP CONSTRAINT "CEM_paciente_idDoctor_id_90b92cdb_fk_CEM_doctor_idDoctor";
       public       DSI    false    220    218    2826                       2606    16482 O   auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 y   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm;
       public       DSI    false    201    2784    205                       2606    16477 P   auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id;
       public       DSI    false    205    203    2789                       2606    16468 E   auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 o   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co;
       public       DSI    false    199    2779    201                       2606    16497 D   auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 n   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id;
       public       DSI    false    209    2789    203                       2606    16492 B   auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id;
       public       DSI    false    2797    207    209                       2606    16511 S   auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 }   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm;
       public       DSI    false    201    2784    211                       2606    16506 V   auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id;
       public       DSI    false    2797    207    211                       2606    16532 G   django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 q   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co;
       public       DSI    false    2779    199    213                       2606    16537 B   django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id;
       public       DSI    false    2797    213    207            �   \   x�3�420��50�54��!csN�5G� 1935�$U�H�*^�W���X�����^�Y���X���Z��������i�i����� a��      �   �   x��;
1F���^��HL���X)�\�%�d��2�r	n�Gw��cq�Hv+g:Y��+�T1öD�ZM���Y�1���Wަ���Z�>�(��N����j����N���oj��L{���'u1J�C�(R      �   �   x�-�;�0D�z���~6��.�B4�e���(v�$,�5�1§����YZ+ep��	�ca8ǐ�3���R���S ��5Ԭ�i�r�1��3O��6r���������������V:��'i���R!���*W      �      x������ � �      �      x������ � �      �   p  x�]�[n�0E��U��*6y��mT�X)R
�V�}��z�1�#͑�%��v�ھ��ӭJ�:����s�i����o�Py%`M`��i�`^	x$�gH�{-:��#��ò��"����a�؋�3,{EC���������j�oZ���H�N��(* <�l�\��$�������3p���x�r�t:?^�r7��Z��=�;�V��W-��!d�F{�x�i>DsG��a[/)�z&aL>��O�L��c���#��m7l��]r�1�hk.T)9�����3�.X�7C�Nxy���]K�4�����P+��˴��'�h�,X	�����u�]C^y�i>p*�i?C�)��! o��<b�e      �   �   x�e�K�@F�3���[ǹ�W	A!\���G6�Y�a��f�Y}���YܪO���v4@���)⻮��K5�h������oǬv��0u]Si��"#_v��!xX.	rX���f�=�=����$#�� �=!��o�V���|��9���dh!X����(�?k/�      �      x������ � �      �      x������ � �      �   �   x�m̱�0�����4w-��n�GpT�*]�	�`�.]	�|?�F�5ښH���8��T�p��>�}�bץ�
rY�'x ���C��cC�E��8�!x޼�y�n�#&6�[��a��s���I�Y������C	!��0�      �   v   x�M˻�0����a�ʥ��y�(�J�6�lg���Bb�g��0�)�"3g�G
�?TX�d�$�f�Zp�Q����e��`$�^������S1n����x��s��x |֑2n      �   �  x���K�!���S�nUQ<{e����M<H�p<��}���GqG��?��lNӘ������ І1�����#�#�7��S�Z�:�<�����^´\d�$�q�!�����D���K.t����7o���u��6Cr�z�x0���9�N)L��ջ�=�N�<�Z P��O��g5�[v����BD�ښZ�1���g{��b,%��ܻ��xɧ6Q$�4�W�Q��?���Rt�D�bV
�J)K-g��m=�s��j��!�2zSQrg�~c�B�U�q��,��-̫ݪ�g����
y<Ou�������4�:|?��l���c�Kc������Y�R_I�I���'��M����}��\r�T ��?~n%�s:�N��$�嫣�L��ӕ� -ɿ�$;�[�hL��= �V4E      �     x�=�Kn�0 ��)z��B� uEK����$�c��IN�B�nG#͘p������t�U:j��'��Σ[\?��7����zẐKD3rU�&���f<�L�TG[�_~��J��2杖y�K���F��J��*3u%�/}j�`G-������������U��$G�i��m�
X��-7
�}�v>��7Kq	��`L	�GSg�,����+cz�y�@Z�������Fl�u�zy��� y�h��I�1���F�(�~ �i|     