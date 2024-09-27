
#https://stem.torproject.org/api/descriptor/server_descriptor.html
import sys
from stem.descriptor import DocumentHandler, parse_file
import stem.control
from stem.descriptor.remote import DescriptorDownloader
from stem.version import Version
import os
import time
import ipinfo


access_token = '2701e46308e262'
handler = ipinfo.getHandler(access_token)

downloader = DescriptorDownloader()

f = open("exit.txt", "w")

others=0
ASCENSION_ISLANDS_ac=0
AFGHANISTAN_af=0
ALAND_ax=0
ALBANIA_al=0
ALGERIA_dz=0
ANDORRA_ad=0
ANGOLA_ao=0
ANGUILLA_ai=0
ANTARCTICA_aq=0
ANTIGUA_AND_BARBUDA_ag=0
ARGENTINA_REPUBLIC_ar=0
ARMENIA_am=0
ARUBA_aw=0
AUSTRALIA_au=0
AUSTRIA_at=0
AZERBAIJAN_az=0
BAHAMAS_bs=0
BAHRAIN_bh=0
BANGLADESH_bd=0
BARBADOS_bb=0
BELARUS_by=0
BELGIUM_be=0
BELIZE_bz=0
BENIN_bj=0
BERMUDA_bm=0
BHUTAN_bt=0
BOLIVIA_bo=0
BOSNIA_AND_HERZEGOVINA_ba=0
BOTSWANA_bw=0
BOUVET_ISLAND_bv=0
BRAZIL_br=0
BRITISH_INDIAN_OCEAN_TERR_io=0
BRITISH_VIRGIN_ISLANDS_vg=0
BRUNEI_DARUSSALAM_bn=0
BULGARIA_bg=0
BURKINA_FASO_bf=0
BURUNDI_bi=0
CAMBODIA_kh=0
CAMEROON_cm=0
CANADA_ca=0
CAPE_VERDE_cv=0
CAYMAN_ISLANDS_ky=0
CENTRAL_AFRICAN_REPUBLIC_cf=0
CHAD_td=0
CHILE_cl=0
CHINA_cn=0
CHRISTMAS_ISLANDS_cx=0
COCOS_ISLANDS_cc=0
COLOMBIA_co=0
COMORAS_km=0
CONGO_cg=0
COOK_ISLANDS_ck=0
COSTA_RICA_cr=0
COTE_D_IVOIRE_ci=0
CROATIA_hr=0
CUBA_cu=0
CYPRUS_cy=0
CZECH_REPUBLIC_cz=0
DENMARK_dk=0
DJIBOUTI_dj=0
DOMINICA_dm=0
DOMINICAN_REPUBLIC_do=0
EAST_TIMOR_tp=0
ECUADOR_ec=0
EGYPT_eg=0
EL_SALVADOR_sv=0
EQUATORIAL_GUINEA_gq=0
ESTONIA_ee=0
ETHIOPIA_et=0
FALKLAND_ISLANDS_fk=0
FAROE_ISLANDS_fo=0
FIJI_fj=0
FINLAND_fi=0
FRANCE_fr=0
FRANCE_METROPOLITAN_fx=0
FRENCH_GUIANA_gf=0
FRENCH_POLYNESIA_pf=0
FRENCH_SOUTHERN_TERRITORIES_tf=0
GABON_ga=0
GAMBIA_gm=0
GEORGIA_ge=0
GERMANY_de=0
GHANA_gh=0
GIBRALTER_gi=0
GREECE_gr=0
GREENLAND_gl=0
GRENADA_gd=0
GUADELOUPE_gp=0
GUAM_gu=0
GUATEMALA_gt=0
GUINEA_gn=0
GUINEA_BISSAU_gw=0
GUYANA_gy=0
HAITI_ht=0
HEARD_MCDONALD_ISLAND_hm=0
HONDURAS_hn=0
HONG_KONG_hk=0
HUNGARY_hu=0
ICELAND_is=0
INDIA_in=0
INDONESIA_id=0
IRAN_ir=0
IRAQ_iq=0
IRELAND_ie=0
ISLE_OF_MAN_im=0
ISRAEL_il=0
ITALY_it=0
JAMAICA_jm=0
JAPAN_jp=0
JORDAN_jo=0
KAZAKHSTAN_kz=0
KENYA_ke=0
KIRIBATI_ki=0
KOREA_kp_kr=0
KUWAIT_kw=0
KYRGYZSTAN_kg=0
LAO_la=0
LATVIA_lv=0
LEBANON_lb=0
LESOTHO_ls=0
LIBERIA_lr=0
LIBYAN_ly=0
LIECHTENSTEIN_li=0
LITHUANIA_lt=0
LUXEMBOURG_lu=0
MACAO_mo=0
MACEDONIA_mk=0
MADAGASCAR_mg=0
MALAWI_mw=0
MALAYSIA_my=0
MALDIVES_mv=0
MALI_ml=0
MALTA_mt=0
MARSHALL_ISLANDS_mh=0
MARTINIQUE_mq=0
MAURITANIA_mr=0
MAURITIUS_mu=0
MAYOTTE_yt=0
MEXICO_mx=0
MICRONESIA_fm=0
MOLDAVA_REPUBLIC_OF_md=0
MONACO_mc=0
MONGOLIA_mn=0
MONTENEGRO_me=0
MONTSERRAT_ms=0
MOROCCO_ma=0
MOZAMBIQUE_mz=0
MYANMAR_mm=0
NAMIBIA_na=0
NAURU_nr=0
NEPAL_np=0
NETHERLANDS_ANTILLES_an=0
NETHERLANDS_nl=0
NEW_CALEDONIA_nc=0
NEW_ZEALAND_nz=0
NICARAGUA_ni=0
NIGER_ne=0
NIGERIA_ng=0
NIUE_nu=0
NORFOLK_ISLAND_nf=0
NORTHERN_MARIANA_ISLANDS_mp=0
NORWAY_no=0
OMAN_om=0
PAKISTAN_pk=0
PALAU_pw=0
PALESTINE_ps=0
PANAMA_pa=0
PAPUA_NEW_GUINEA_pg=0
PARAGUAY_py=0
PERU_pe=0
PHILIPPINES_ph=0
PITCAIRN_pn=0
POLAND_pl=0
PORTUGAL_pt=0
PUERTO_RICO_pr=0
QATAR_qa=0
REUNION_re=0
ROMANIA_ro=0
RUSSIAN_FEDERATION_ru=0
RWANDA_rw=0
SAMOA_ws=0
SAN_MARINO_sm=0
SAO_TOME_PRINCIPE_st=0
SAUDI_ARABIA_sa=0
SCOTLAND_uk=0
SENEGAL_sn=0
SERBIA_rs=0
SEYCHELLES_sc=0
SIERRA_LEONE_sl=0
SINGAPORE_sg=0
SLOVAKIA_sk=0
SLOVENIA_si=0
SOLOMON_ISLANDS_sb=0
SOMALIA_so=0
SOMOA_GILBERT_ELLICE_ISLANDS_as=0
SOUTH_AFRICA_za=0
SOUTH_GEORGIA_SOUTH_SANDWICH_ISLANDS_gs=0
SOVIET_UNION_su=0
SPAIN_es=0
SRI_LANKA_lk=0
ST_HELENA_sh=0
ST_KITTS_AND_NEVIS_kn=0
ST_LUCIA_lc=0
ST_PIERRE_AND_MIQUELON_pm=0
ST_VINCENT_THE_GRENADINES_vc=0
SUDAN_sd=0
SURINAME_sr=0
SVALBARD_AND_JAN_MAYEN_sj=0
SWAZILAND_sz=0
SWEDEN_se=0
SWITZERLAND_ch=0
SYRIAN_ARAB_REPUBLIC_sy=0
TAIWAN_tw=0
TAJIKISTAN_tj=0
TANZANIA_tz=0
THAILAND_th=0
TOGO_tg=0
TOKELAU_tk=0
TONGA_to=0
TRINIDADANDTOBAGO_tt=0
TUNISIA_tn=0
TURKEY_tr=0
TURKMENISTAN_tm=0
TURKS_AND_CALCOS_ISLANDS_tc=0
TUVALU_tv=0
UGANDA_ug=0
UKRAINE_ua=0
UNITED_ARAB_EMIRATES_ae=0
UNITED_KINGDOM_gb=0
UNITED_STATES_us=0
UNITED_STATES_MINOR_OUTL_um=0
URUGUAY_uy=0
UZBEKISTAN_uz=0
VANUATU_vu=0
VATICAN_CITY_STATE_va=0
VENEZUELA_ve=0
VIETNAM_vn=0
VIRGIN_ISLANDS_vi=0
WALLIS_AND_FUTUNA_ISLANDS_wf=0
WESTERN_SAHARA_eh=0
YEMEN_ye=0
ZAMBIA_zm=0
ZIMBABWE_zw=0

#consensus = downloader.get_consensus(document_handler = DocumentHandler.DOCUMENT).run()[0]

consensus = next(parse_file('/tmp/descriptor_dump', descriptor_type = 'network-status-consensus-3 1.0', document_handler = DocumentHandler.DOCUMENT,))

with stem.control.Controller.from_port() as controller:
 controller.authenticate()
 relay_fingerprints=""
 relay_bandwidth = []
 relay_compare = []
 print("CHECKING THE IP!")
 
 for desc in downloader.get_server_descriptors():
  handler = ipinfo.getHandler(access_token)
  details = handler.getDetails(desc.address)
  time.sleep(0.25)
  for fingerprint, relay in consensus.routers.items():
    if(details.country.casefold() in "ac" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     ASCENSION_ISLANDS_ac+=1
    elif(details.country.casefold() in "af" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     AFGHANISTAN_af+=1
    elif(details.country.casefold() in "ax" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     ALAND_ax+=1
    elif(details.country.casefold() in "al" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     ALBANIA_al+=1
    elif(details.country.casefold() in "dz" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     ALGERIA_dz+=1
    elif(details.country.casefold() in "ad" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     ANDORRA_ad+=1
    elif(details.country.casefold() in "ao" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     ANGOLA_ao+=1
    elif(details.country.casefold() in "ai" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     ANGUILLA_ai+=1
    elif(details.country.casefold() in "aq" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     ANTARCTICA_aq+=1
    elif(details.country.casefold() in "ag" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     ANTIGUA_AND_BARBUDA_ag+=1
    elif(details.country.casefold() in "ar" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     ARGENTINA_REPUBLIC_ar+=1
    elif(details.country.casefold() in "am" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     ARMENIA_am+=1
    elif(details.country.casefold() in "aw" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     ARUBA_aw+=1
    elif(details.country.casefold() in "au" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     AUSTRALIA_au+=1
    elif(details.country.casefold() in "at" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     AUSTRIA_at+=1
    elif(details.country.casefold() in "az" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     AZERBAIJAN_az+=1
    elif(details.country.casefold() in "bs" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     BAHAMAS_bs+=1
    elif(details.country.casefold() in "bh" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     BAHRAIN_bh+=1
    elif(details.country.casefold() in "bd" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     BANGLADESH_bd+=1
    elif(details.country.casefold() in "bb" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     BARBADOS_bb+=1
    elif(details.country.casefold() in "by" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     BELARUS_by+=1
    elif(details.country.casefold() in "be" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     BELGIUM_be+=1
    elif(details.country.casefold() in "bz" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     BELIZE_bz+=1
    elif(details.country.casefold() in "bj" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     BENIN_bj+=1
    elif(details.country.casefold() in "bm" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     BERMUDA_bm+=1
    elif(details.country.casefold() in "bt" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     BHUTAN_bt+=1
    elif(details.country.casefold() in "bo" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     BOLIVIA_bo+=1
    elif(details.country.casefold() in "ba" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     BOSNIA_AND_HERZEGOVINA_ba+=1
    elif(details.country.casefold() in "bw" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     BOTSWANA_bw+=1
    elif(details.country.casefold() in "bv" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     BOUVET_ISLAND_bv+=1
    elif(details.country.casefold() in "br" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     BRAZIL_br+=1
    elif(details.country.casefold() in "io" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     BRITISH_INDIAN_OCEAN_TERR_io+=1
    elif(details.country.casefold() in "vg" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     BRITISH_VIRGIN_ISLANDS_vg+=1
    elif(details.country.casefold() in "bn" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     BRUNEI_DARUSSALAM_bn+=1
    elif(details.country.casefold() in "bg" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     BULGARIA_bg+=1
    elif(details.country.casefold() in "bf" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     BURKINA_FASO_bf+=1
    elif(details.country.casefold() in "bi" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     BURUNDI_bi+=1
    elif(details.country.casefold() in "kh" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     CAMBODIA_kh+=1
    elif(details.country.casefold() in "cm" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     CAMEROON_cm+=1
    elif(details.country.casefold() in "ca" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     CANADA_ca+=1
    elif(details.country.casefold() in "cv" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     CAPE_VERDE_cv+=1
    elif(details.country.casefold() in "ky" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     CAYMAN_ISLANDS_ky+=1
    elif(details.country.casefold() in "cf" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     CENTRAL_AFRICAN_REPUBLIC_cf+=1
    elif(details.country.casefold() in "td" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     CHAD_td+=1
    elif(details.country.casefold() in "cl" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     CHILE_cl+=1
    elif(details.country.casefold() in "cn" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     CHINA_cn+=1
    elif(details.country.casefold() in "cx" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     CHRISTMAS_ISLANDS_cx+=1
    elif(details.country.casefold() in "cc" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     COCOS_ISLANDS_cc+=1
    elif(details.country.casefold() in "co" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     COLOMBIA_co+=1
    elif(details.country.casefold() in "km" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     COMORAS_km+=1
    elif(details.country.casefold() in "cg" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     CONGO_cg+=1
    elif(details.country.casefold() in "ck" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     COOK_ISLANDS_ck+=1
    elif(details.country.casefold() in "cr" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     COSTA_RICA_cr+=1
    elif(details.country.casefold() in "ci" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     COTE_D_IVOIRE+=1
    elif(details.country.casefold() in "hr" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     CROATIA_hr+=1
    elif(details.country.casefold() in "cu" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     CUBA_cu+=1
    elif(details.country.casefold() in "cy" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     CYPRUS_cy+=1
    elif(details.country.casefold() in "cz" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     CZECH_REPUBLIC_cz+=1
    elif(details.country.casefold() in "dk" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     DENMARK_dk+=1
    elif(details.country.casefold() in "dj" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     DJIBOUTI_dj+=1
    elif(details.country.casefold() in "dm" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     DOMINICA_dm+=1
    elif(details.country.casefold() in "do" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     DOMINICAN_REPUBLIC_do+=1
    elif(details.country.casefold() in "tp" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     EAST_TIMOR_tp+=1
    elif(details.country.casefold() in "ec" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     ECUADOR_ec+=1
    elif(details.country.casefold() in "eg" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     EGYPT_eg+=1
    elif(details.country.casefold() in "sv" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     EL_SALVADOR_sv+=1
    elif(details.country.casefold() in "gq" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     EQUATORIAL_GUINEA_gq+=1
    elif(details.country.casefold() in "ee" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     ESTONIA_ee+=1
    elif(details.country.casefold() in "et" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     ETHIOPIA_et+=1
    elif(details.country.casefold() in "fk" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     FALKLAND_ISLANDS_fk+=1
    elif(details.country.casefold() in "fo" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     FAROE_ISLANDS_fo+=1
    elif(details.country.casefold() in "fj" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     FIJI_fj+=1
    elif(details.country.casefold() in "fi" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     FINLAND_fi+=1
    elif(details.country.casefold() in "fr" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     FRANCE_fr+=1
    elif(details.country.casefold() in "fx" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     FRANCE_METROPOLITAN_fx+=1
    elif(details.country.casefold() in "gf" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     FRENCH_GUIANA_gf+=1
    elif(details.country.casefold() in "pf" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     FRENCH_POLYNESIA_pf+=1
    elif(details.country.casefold() in "tf" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     FRENCH_SOUTHERN_TERRITORIES_tf+=1
    elif(details.country.casefold() in "ga" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     GABON_ga+=1
    elif(details.country.casefold() in "gm" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     GAMBIA_gm+=1
    elif(details.country.casefold() in "ge" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     GEORGIA_ge+=1
    elif(details.country.casefold() in "de" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     GERMANY_de+=1
    elif(details.country.casefold() in "gh" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     GHANA_gh+=1
    elif(details.country.casefold() in "gi" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     GIBRALTER_gi+=1
    elif(details.country.casefold() in "gr" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     GREECE_gr+=1
    elif(details.country.casefold() in "gl" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     GREENLAND_gl+=1
    elif(details.country.casefold() in "gd" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     GRENADA_gd+=1
    elif(details.country.casefold() in "gp" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     GUADELOUPE_gp+=1
    elif(details.country.casefold() in "gu" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     GUAM_gu+=1
    elif(details.country.casefold() in "gt" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     GUATEMALA_gt+=1
    elif(details.country.casefold() in "gn" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     GUINEA_gn+=1
    elif(details.country.casefold() in "gw" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     GUINEA_BISSAU_gw+=1
    elif(details.country.casefold() in "gy" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     GUYANA_gy+=1
    elif(details.country.casefold() in "ht" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     HAITI_ht+=1
    elif(details.country.casefold() in "hm" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     HEARD_MCDONALD_ISLAND_hm+=1
    elif(details.country.casefold() in "hn" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     HONDURAS_hn+=1
    elif(details.country.casefold() in "hk" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     HONG_KONG_hk+=1
    elif(details.country.casefold() in "hu" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     HUNGARY_hu+=1
    elif(details.country.casefold() in "is" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     ICELAND_is+=1
    elif(details.country.casefold() in "in" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     INDIA_in+=1
    elif(details.country.casefold() in "id" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     INDONESIA_id+=1
    elif(details.country.casefold() in "ir" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     IRAN_ir+=1
    elif(details.country.casefold() in "iq" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     IRAQ_iq+=1
    elif(details.country.casefold() in "ie" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     IRELAND_ie+=1
    elif(details.country.casefold() in "im" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     ISLE_OF_MAN_im+=1
    elif(details.country.casefold() in "il" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     ISRAEL_il+=1
    elif(details.country.casefold() in "it" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     ITALY_it+=1
    elif(details.country.casefold() in "jm" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     JAMAICA_jm+=1
    elif(details.country.casefold() in "jp" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     JAPAN_jp+=1
    elif(details.country.casefold() in "jo" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     JORDAN_jo+=1
    elif(details.country.casefold() in "kz" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     KAZAKHSTAN_kz+=1
    elif(details.country.casefold() in "ke" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     KENYA_ke+=1
    elif(details.country.casefold() in "ki" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     KIRIBATI_ki+=1
    elif(details.country.casefold() in "kr" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     KOREA_kp_kr+=1
    elif(details.country.casefold() in "kw" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     KUWAIT_kw+=1
    elif(details.country.casefold() in "kg" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     KYRGYZSTAN_kg+=1
    elif(details.country.casefold() in "la" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     LAO_la+=1
    elif(details.country.casefold() in "lv" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     LATVIA_lv+=1
    elif(details.country.casefold() in "lb" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     LEBANON_lb+=1
    elif(details.country.casefold() in "ls" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     LESOTHO_ls+=1
    elif(details.country.casefold() in "lr" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     LIBERIA_lr+=1
    elif(details.country.casefold() in "ly" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     LIBYAN_ly+=1
    elif(details.country.casefold() in "li" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     LIECHTENSTEIN_li+=1
    elif(details.country.casefold() in "lt" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     LITHUANIA_lt+=1
    elif(details.country.casefold() in "lu" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     LUXEMBOURG_lu+=1
    elif(details.country.casefold() in "mo" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     MACAO_mo+=1
    elif(details.country.casefold() in "mk" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     MACEDONIA_mk+=1
    elif(details.country.casefold() in "mg" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     MADAGASCAR_mg+=1
    elif(details.country.casefold() in "mw" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     MALAWI_mw+=1
    elif(details.country.casefold() in "my" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     MALAYSIA_my+=1
    elif(details.country.casefold() in "mv" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     MALDIVES_mv+=1
    elif(details.country.casefold() in "ml" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     MALI_ml+=1
    elif(details.country.casefold() in "mt" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     MALTA_mt+=1
    elif(details.country.casefold() in "mh" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     MARSHALL_ISLANDS_mh+=1
    elif(details.country.casefold() in "mq" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     MARTINIQUE_mq+=1
    elif(details.country.casefold() in "mr" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     MAURITANIA_mr+=1
    elif(details.country.casefold() in "mu" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     MAURITIUS_mu+=1
    elif(details.country.casefold() in "yt" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     MAYOTTE_yt+=1
    elif(details.country.casefold() in "mx" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     MEXICO_mx+=1
    elif(details.country.casefold() in "fm" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     MICRONESIA_fm+=1
    elif(details.country.casefold() in "md" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     MOLDAVA_REPUBLIC_OF_md+=1
    elif(details.country.casefold() in "mc" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     MONACO_mc+=1
    elif(details.country.casefold() in "mn" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     MONGOLIA_mn+=1
    elif(details.country.casefold() in "me" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     MONTENEGRO_me+=1
    elif(details.country.casefold() in "ms" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     MONTSERRAT_ms+=1
    elif(details.country.casefold() in "ma" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     MOROCCO_ma+=1
    elif(details.country.casefold() in "mz" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     MOZAMBIQUE_mz+=1
    elif(details.country.casefold() in "mm" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     MYANMAR_mm+=1
    elif(details.country.casefold() in "na" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     NAMIBIA_na+=1
    elif(details.country.casefold() in "nr" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     NAURU_nr+=1
    elif(details.country.casefold() in "np" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     NEPAL_np+=1
    elif(details.country.casefold() in "an" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     NETHERLANDS_ANTILLES_an+=1
    elif(details.country.casefold() in "nl" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     NETHERLANDS_nl+=1
    elif(details.country.casefold() in "nc" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     NEW_CALEDONIA_nc+=1
    elif(details.country.casefold() in "nz" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     NEW_ZEALAND_nz+=1
    elif(details.country.casefold() in "ni" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     NICARAGUA_ni+=1
    elif(details.country.casefold() in "ne" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     NIGER_ne+=1
    elif(details.country.casefold() in "ng" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     NIGERIA_ng+=1
    elif(details.country.casefold() in "nu" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     NIUE_nu+=1
    elif(details.country.casefold() in "nf" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     NORFOLK_ISLAND_nf+=1
    elif(details.country.casefold() in "mp" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     NORTHERN_MARIANA_ISLANDS_mp+=1
    elif(details.country.casefold() in "no" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     NORWAY_no+=1
    elif(details.country.casefold() in "om" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     OMAN_om+=1
    elif(details.country.casefold() in "pk" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     PAKISTAN_pk+=1
    elif(details.country.casefold() in "pw" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     PALAU_pw+=1
    elif(details.country.casefold() in "ps" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     PALESTINE_ps+=1
    elif(details.country.casefold() in "pa" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     PANAMA_pa+=1
    elif(details.country.casefold() in "pg" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     PAPUA_NEW_GUINEA_pg+=1
    elif(details.country.casefold() in "py" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     PARAGUAY_py+=1
    elif(details.country.casefold() in "pe" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     PERU_pe+=1
    elif(details.country.casefold() in "ph" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     PHILIPPINES_ph+=1
    elif(details.country.casefold() in "pn" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     PITCAIRN_pn+=1
    elif(details.country.casefold() in "pl" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     POLAND_pl+=1
    elif(details.country.casefold() in "pt" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     PORTUGAL_pt+=1
    elif(details.country.casefold() in "pr" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     PUERTO_RICO_pr+=1
    elif(details.country.casefold() in "qa" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     QATAR_qa+=1
    elif(details.country.casefold() in "re" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     REUNION_re+=1
    elif(details.country.casefold() in "ro" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     ROMANIA_ro+=1
    elif(details.country.casefold() in "ru" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     RUSSIAN_FEDERATION_ru+=1
    elif(details.country.casefold() in "rw" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     RWANDA_rw+=1
    elif(details.country.casefold() in "ws" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     SAMOA_ws+=1
    elif(details.country.casefold() in "sm" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     SAN_MARINO_sm+=1
    elif(details.country.casefold() in "st" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     SAO_TOME_PRINCIPE_st+=1
    elif(details.country.casefold() in "sa" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     SAUDI_ARABIA_sa+=1
    elif(details.country.casefold() in "uk" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     SCOTLAND_uk+=1
    elif(details.country.casefold() in "sn" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     SENEGAL_sn+=1
    elif(details.country.casefold() in "rs" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     SERBIA_rs+=1
    elif(details.country.casefold() in "sc" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     SEYCHELLES_sc+=1
    elif(details.country.casefold() in "sl" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     SIERRA_LEONE_sl+=1
    elif(details.country.casefold() in "sg" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     SINGAPORE_sg+=1
    elif(details.country.casefold() in "sk" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     SLOVAKIA_sk+=1
    elif(details.country.casefold() in "si" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     SLOVENIA_si+=1
    elif(details.country.casefold() in "sb" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     SOLOMON_ISLANDS_sb+=1
    elif(details.country.casefold() in "so" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     SOMALIA_so+=1
    elif(details.country.casefold() in "as" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     SOMOA_GILBERT_ELLICE_ISLANDS_as+=1
    elif(details.country.casefold() in "za" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     SOUTH_AFRICA_za+=1
    elif(details.country.casefold() in "gs" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     SOUTH_GEORGIA_SOUTH_SANDWICH_ISLANDS_gs+=1
    elif(details.country.casefold() in "su" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     SOVIET_UNION_su+=1
    elif(details.country.casefold() in "es" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     SPAIN_es+=1
    elif(details.country.casefold() in "lk" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     SRI_LANKA_lk+=1
    elif(details.country.casefold() in "sh" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     ST_HELENA_sh+=1
    elif(details.country.casefold() in "kn" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     ST_KITTS_AND_NEVIS_kn+=1
    elif(details.country.casefold() in "lc" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     ST_LUCIA_lc+=1
    elif(details.country.casefold() in "pm" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     ST_PIERRE_AND_MIQUELON_pm+=1
    elif(details.country.casefold() in "vc" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     ST_VINCENT_THE_GRENADINES_vc+=1
    elif(details.country.casefold() in "sd" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     SUDAN_sd+=1
    elif(details.country.casefold() in "sr" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     SURINAME_sr+=1
    elif(details.country.casefold() in "sj" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     SVALBARD_AND_JAN_MAYEN_sj+=1
    elif(details.country.casefold() in "sz" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     SWAZILAND_sz+=1
    elif(details.country.casefold() in "se" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     SWEDEN_se+=1
    elif(details.country.casefold() in "ch" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     SWITZERLAND_ch+=1
    elif(details.country.casefold() in "sy" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     SYRIAN_ARAB_REPUBLIC_sy+=1
    elif(details.country.casefold() in "tw" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     TAIWAN_tw+=1
    elif(details.country.casefold() in "tj" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     TAJIKISTAN_tj+=1
    elif(details.country.casefold() in "tz" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     TANZANIA_tz+=1
    elif(details.country.casefold() in "th" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     THAILAND_th+=1
    elif(details.country.casefold() in "tg" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     TOGO_tg+=1
    elif(details.country.casefold() in "tk" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     TOKELAU_tk+=1
    elif(details.country.casefold() in "to" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     TONGA_to+=1
    elif(details.country.casefold() in "tt" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     TRINIDADANDTOBAGO_tt+=1
    elif(details.country.casefold() in "tn" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     TUNISIA_tn+=1
    elif(details.country.casefold() in "tr" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     TURKEY_tr+=1
    elif(details.country.casefold() in "tm" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     TURKMENISTAN_tm+=1
    elif(details.country.casefold() in "tc" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     TURKS_AND_CALCOS_ISLANDS_tc+=1
    elif(details.country.casefold() in "tv" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     TUVALU_tv+=1
    elif(details.country.casefold() in "ug" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     UGANDA_ug+=1
    elif(details.country.casefold() in "ua" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     UKRAINE_ua+=1
    elif(details.country.casefold() in "ae" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     UNITED_ARAB_EMIRATES_ae+=1
    elif(details.country.casefold() in "gb" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     UNITED_KINGDOM_gb+=1
    elif(details.country.casefold() in "us" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     UNITED_STATES_us+=1
    elif(details.country.casefold() in "um" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     UNITED_STATES_MINOR_OUTL_um+=1
    elif(details.country.casefold() in "uy" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     URUGUAY_uy+=1
    elif(details.country.casefold() in "uz" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     UZBEKISTAN_uz+=1
    elif(details.country.casefold() in "vu" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     VANUATU_vu+=1
    elif(details.country.casefold() in "va" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     VATICAN_CITY_STATE_va+=1
    elif(details.country.casefold() in "ve" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     VENEZUELA_ve+=1
    elif(details.country.casefold() in "vn" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     VIETNAM_vn+=1
    elif(details.country.casefold() in "vi" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     VIRGIN_ISLANDS_vi+=1
    elif(details.country.casefold() in "wf" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     WALLIS_AND_FUTUNA_ISLANDS_wf+=1
    elif(details.country.casefold() in "eh" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     WESTERN_SAHARA_eh+=1
    elif(details.country.casefold() in "ye" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     YEMEN_ye+=1
    elif(details.country.casefold() in "zm" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     ZAMBIA_zm+=1
    elif(details.country.casefold() in "zw" and desc.fingerprint in fingerprint and "Exit" in relay.flags):
     ZIMBABWE_zw+=1
    else:
      others+=1

f.write( str(ASCENSION_ISLANDS_ac)+"\n" + str(AFGHANISTAN_af)+"\n"+ str(ALAND_ax)+"\n" +str(ALBANIA_al)+"\n"+str(ALGERIA_dz)+"\n"+str(ANDORRA_ad)+"\n"+str(ANGOLA_ao)+"\n"+str(ANGUILLA_ai)+"\n"+str(ANTARCTICA_aq)+"\n"+str(ANTIGUA_AND_BARBUDA_ag)+"\n"+str(ARGENTINA_REPUBLIC_ar)+"\n"+str(ARMENIA_am)+"\n"+str(ARUBA_aw)+"\n"+str(AUSTRALIA_au)+"\n"+str(AUSTRIA_at)+"\n"+str(AZERBAIJAN_az)+"\n"+str(BAHAMAS_bs)+"\n"+str(BAHRAIN_bh)+"\n"+str(BANGLADESH_bd)+"\n"+str(BARBADOS_bb)+"\n"+str(BELARUS_by)+"\n"+str(BELGIUM_be)+"\n"+str(BELIZE_bz)+"\n"+str(BENIN_bj)+"\n"+str(BERMUDA_bm)+"\n"+str(BHUTAN_bt)+"\n"+str(BOLIVIA_bo)+"\n"+str(BOSNIA_AND_HERZEGOVINA_ba)+"\n"+str(BOTSWANA_bw)+"\n"+str(BOUVET_ISLAND_bv)+"\n"+str(BRAZIL_br)+"\n"+str(BRITISH_INDIAN_OCEAN_TERR_io)+"\n"+str(BRITISH_VIRGIN_ISLANDS_vg)+"\n"+str(BRUNEI_DARUSSALAM_bn)+"\n"+str(BULGARIA_bg)+"\n"+str(BURKINA_FASO_bf)+"\n"+str(BURUNDI_bi)+"\n"+str(CAMBODIA_kh)+"\n"+str(CAMEROON_cm)+"\n"+str(CANADA_ca)+"\n"+str(CAPE_VERDE_cv)+"\n"+str(CAYMAN_ISLANDS_ky)+"\n"+str(CENTRAL_AFRICAN_REPUBLIC_cf)+"\n"+str(CHAD_td)+"\n"+str(CHILE_cl)+"\n"+str(CHINA_cn)+"\n"+str(CHRISTMAS_ISLANDS_cx)+"\n"+str(COCOS_ISLANDS_cc)+"\n"+str(COLOMBIA_co)+"\n"+str(COMORAS_km)+"\n"+str(CONGO_cg)+"\n"+str(COOK_ISLANDS_ck)+"\n"+str(COSTA_RICA_cr)+"\n"+str(COTE_D_IVOIRE_ci)+"\n"+str(CROATIA_hr)+"\n"+str(CUBA_cu)+"\n"+str(CYPRUS_cy)+"\n"+str(CZECH_REPUBLIC_cz)+"\n"+str(DENMARK_dk)+"\n"+str(DJIBOUTI_dj)+"\n"+str(DOMINICA_dm)+"\n"+str(DOMINICAN_REPUBLIC_do)+"\n"+str(EAST_TIMOR_tp)+"\n"+str(ECUADOR_ec)+"\n"+str(EGYPT_eg)+"\n"+str(EL_SALVADOR_sv)+"\n"+str(EQUATORIAL_GUINEA_gq)+"\n"+str(ESTONIA_ee)+"\n"+str(ETHIOPIA_et)+"\n"+str(FALKLAND_ISLANDS_fk)+"\n"+str(FAROE_ISLANDS_fo)+"\n"+str(FIJI_fj)+"\n"+str(FINLAND_fi)+"\n"+str(FRANCE_fr)+"\n"+str(FRANCE_METROPOLITAN_fx)+"\n"+str(FRENCH_GUIANA_gf)+"\n"+str(FRENCH_POLYNESIA_pf)+"\n"+str(FRENCH_SOUTHERN_TERRITORIES_tf)+"\n"+str(GABON_ga)+"\n"+str(GAMBIA_gm)+"\n"+str(GEORGIA_ge)+"\n"+str(GERMANY_de)+"\n"+str(GHANA_gh)+"\n"+str(GIBRALTER_gi)+"\n"+str(GREECE_gr)+"\n"+str(GREENLAND_gl)+"\n"+str(GRENADA_gd)+"\n"+str(GUADELOUPE_gp)+"\n"+str(GUAM_gu)+"\n"+str(GUATEMALA_gt)+"\n"+str(GUINEA_gn)+"\n"+str(GUINEA_BISSAU_gw)+"\n"+str(GUYANA_gy)+"\n"+str(HAITI_ht)+"\n"+str(HEARD_MCDONALD_ISLAND_hm)+"\n"+str(HONDURAS_hn)+"\n"+str(HONG_KONG_hk)+"\n"+str(HUNGARY_hu)+"\n"+str(ICELAND_is)+"\n"+str(INDIA_in)+"\n"+str(INDONESIA_id)+"\n"+str(IRAN_ir)+"\n"+str(IRAQ_iq)+"\n"+str(IRELAND_ie)+"\n"+str(ISLE_OF_MAN_im)+"\n"+str(ISRAEL_il)+"\n"+str(ITALY_it)+"\n"+str(JAMAICA_jm)+"\n"+str(JAPAN_jp)+"\n"+str(JORDAN_jo)+"\n"+str(KAZAKHSTAN_kz)+"\n"+str(KENYA_ke)+"\n"+str(KIRIBATI_ki)+"\n"+str(KOREA_kp_kr)+"\n"+str(KUWAIT_kw)+"\n"+str(KYRGYZSTAN_kg)+"\n"+str(LAO_la)+"\n"+str(LATVIA_lv)+"\n"+str(LEBANON_lb)+"\n"+str(LESOTHO_ls)+"\n"+str(LIBERIA_lr)+"\n"+str(LIBYAN_ly)+"\n"+str(LIECHTENSTEIN_li)+"\n"+str(LITHUANIA_lt)+"\n"+str(LUXEMBOURG_lu)+"\n"+str(MACAO_mo)+"\n"+str(MACEDONIA_mk)+"\n"+str(MADAGASCAR_mg)+"\n"+str(MALAWI_mw)+"\n"+str(MALAYSIA_my)+"\n"+str(MALDIVES_mv)+"\n"+str(MALI_ml)+"\n"+str(MALTA_mt)+"\n"+str(MARSHALL_ISLANDS_mh)+"\n"+str(MARTINIQUE_mq)+"\n"+str(MAURITANIA_mr)+"\n"+str(MAURITIUS_mu)+"\n"+str(MAYOTTE_yt)+"\n"+str(MEXICO_mx)+"\n"+str(MICRONESIA_fm)+"\n"+str(MOLDAVA_REPUBLIC_OF_md)+"\n"+str(MONACO_mc)+"\n"+str(MONGOLIA_mn)+"\n"+str(MONTENEGRO_me)+"\n"+str(MONTSERRAT_ms)+"\n"+str(MOROCCO_ma)+"\n"+str(MOZAMBIQUE_mz)+"\n"+str(MYANMAR_mm)+"\n"+str(NAMIBIA_na)+"\n"+str(NAURU_nr)+"\n"+str(NEPAL_np)+"\n"+str(NETHERLANDS_ANTILLES_an)+"\n"+str(NETHERLANDS_nl)+"\n"+str(NEW_CALEDONIA_nc)+"\n"+str(NEW_ZEALAND_nz)+"\n"+str(NICARAGUA_ni)+"\n"+str(NIGER_ne)+"\n"+str(NIGERIA_ng)+"\n"+str(NIUE_nu)+"\n"+str(NORFOLK_ISLAND_nf)+"\n"+str(NORTHERN_MARIANA_ISLANDS_mp)+"\n"+str(NORWAY_no)+"\n"+str(OMAN_om)+"\n"+str(PAKISTAN_pk)+"\n"+str(PALAU_pw)+"\n"+str(PALESTINE_ps)+"\n"+str(PANAMA_pa)+"\n"+str(PAPUA_NEW_GUINEA_pg)+"\n"+str(PARAGUAY_py)+"\n"+str(PERU_pe)+"\n"+str(PHILIPPINES_ph)+"\n"+str(PITCAIRN_pn)+"\n"+str(POLAND_pl)+"\n"+str(PORTUGAL_pt)+"\n"+str(PUERTO_RICO_pr)+"\n"+str(QATAR_qa)+"\n"+str(REUNION_re)+"\n"+str(ROMANIA_ro)+"\n"+str(RUSSIAN_FEDERATION_ru)+"\n"+str(RWANDA_rw)+"\n"+str(SAMOA_ws)+"\n"+str(SAN_MARINO_sm)+"\n"+str(SAO_TOME_PRINCIPE_st)+"\n"+str(SAUDI_ARABIA_sa)+"\n"+str(SCOTLAND_uk)+"\n"+str(SENEGAL_sn)+"\n"+str(SERBIA_rs)+"\n"+str(SEYCHELLES_sc)+"\n"+str(SIERRA_LEONE_sl)+"\n"+str(SINGAPORE_sg)+"\n"+str(SLOVAKIA_sk)+"\n"+str(SLOVENIA_si)+"\n"+str(SOLOMON_ISLANDS_sb)+"\n"+str(SOMALIA_so)+"\n"+str(SOMOA_GILBERT_ELLICE_ISLANDS_as)+"\n"+str(SOUTH_AFRICA_za)+"\n"+str(SOUTH_GEORGIA_SOUTH_SANDWICH_ISLANDS_gs)+"\n"+str(SOVIET_UNION_su)+"\n"+str(SPAIN_es)+"\n"+str(SRI_LANKA_lk)+"\n"+str(ST_HELENA_sh)+"\n"+str(ST_KITTS_AND_NEVIS_kn)+"\n"+str(ST_LUCIA_lc)+"\n"+str(ST_PIERRE_AND_MIQUELON_pm)+"\n"+str(ST_VINCENT_THE_GRENADINES_vc)+"\n"+str(SUDAN_sd)+"\n"+str(SURINAME_sr)+"\n"+str(SVALBARD_AND_JAN_MAYEN_sj)+"\n"+str(SWAZILAND_sz)+"\n"+str(SWEDEN_se)+"\n"+str(SWITZERLAND_ch)+"\n"+str(SYRIAN_ARAB_REPUBLIC_sy)+"\n"+str(TAIWAN_tw)+"\n"+str(TAJIKISTAN_tj)+"\n"+str(TANZANIA_tz)+"\n"+str(THAILAND_th)+"\n"+str(TOGO_tg)+"\n"+str(TOKELAU_tk)+"\n"+str(TONGA_to)+"\n"+str(TRINIDADANDTOBAGO_tt)+"\n"+str(TUNISIA_tn)+"\n"+str(TURKEY_tr)+"\n"+str(TURKMENISTAN_tm)+"\n"+str(TURKS_AND_CALCOS_ISLANDS_tc)+"\n"+str(TUVALU_tv)+"\n"+str(UGANDA_ug)+"\n"+str(UKRAINE_ua)+"\n"+str(UNITED_ARAB_EMIRATES_ae)+"\n"+str(UNITED_KINGDOM_gb)+"\n"+str(UNITED_STATES_us)+"\n"+str(UNITED_STATES_MINOR_OUTL_um)+"\n"+str(URUGUAY_uy)+"\n"+str(UZBEKISTAN_uz)+"\n"+str(VANUATU_vu)+"\n"+str(VATICAN_CITY_STATE_va)+"\n"+str(VENEZUELA_ve)+"\n"+str(VIETNAM_vn)+"\n"+str(VIRGIN_ISLANDS_vi)+"\n"+str(WALLIS_AND_FUTUNA_ISLANDS_wf)+"\n"+str(WESTERN_SAHARA_eh)+"\n"+str(YEMEN_ye)+"\n"+str(ZAMBIA_zm)+"\n"+str(ZIMBABWE_zw)+"\n"+str(others))
f.close()
os.system("sudo killall tor")