# This file contains minimized db schema and it should not be touched manually but only generated by tools/scripts/generate_minimized_db_schema.py
# Created at 2024-12-05 09:19:46 UTC with rotki version 1.23.5.dev7172+gd55bcd2a5 by prettyirrelevant
MINIMIZED_GLOBAL_DB_SCHEMA = {
    "token_kinds": "token_kindchar(1)primarykeynotnull,seqintegerunique",
    "underlying_tokens_list": "identifiertextnotnull,weighttextnotnull,parent_token_entrytextnotnull,foreignkey(parent_token_entry)referencesevm_tokens(identifier)ondeletecascadeonupdatecascadeforeignkey(identifier)referencesevm_tokens(identifier)onupdatecascadeondeletecascadeprimarykey(identifier,parent_token_entry)",
    "settings": "namevarchar[24]notnullprimarykey,valuetext",
    "asset_types": "typechar(1)primarykeynotnull,seqintegerunique",
    "assets": "identifiertextprimarykeynotnullcollatenocase,nametext,typechar(1)notnulldefault('a')referencesasset_types(type)",
    "evm_tokens": "identifiertextprimarykeynotnullcollatenocase,token_kindchar(1)notnulldefault('a')referencestoken_kinds(token_kind),chainintegernotnull,addressvarchar[42]notnull,decimalsinteger,protocoltext,foreignkey(identifier)referencesassets(identifier)onupdatecascadeondeletecascade",
    "multiasset_mappings": "collection_idintegernotnull,assettextnotnull,foreignkey(collection_id)referencesasset_collections(id)onupdatecascadeondeletecascade,foreignkey(asset)referencesassets(identifier)onupdatecascadeondeletecascade,primarykey(collection_id,asset)",
    "common_asset_details": "identifiertextprimarykeynotnullcollatenocase,symboltext,coingeckotext,cryptocomparetext,forkedtext,startedinteger,swapped_fortext,foreignkey(forked)referencesassets(identifier)onupdatecascadeondeletesetnull,foreignkey(identifier)referencesassets(identifier)onupdatecascadeondeletecascade,foreignkey(swapped_for)referencesassets(identifier)onupdatecascadeondeletesetnull",
    "user_owned_assets": "asset_idvarchar[24]notnullprimarykey,foreignkey(asset_id)referencesassets(identifier)onupdatecascadeondeletecascade",
    "price_history_source_types": "typechar(1)primarykeynotnull,seqintegerunique",
    "price_history": "from_assettextnotnullcollatenocase,to_assettextnotnullcollatenocase,source_typechar(1)notnulldefault('a')referencesprice_history_source_types(type),timestampintegernotnull,pricetextnotnull,foreignkey(from_asset)referencesassets(identifier)onupdatecascadeondeletecascade,foreignkey(to_asset)referencesassets(identifier)onupdatecascadeondeletecascade,primarykey(from_asset,to_asset,source_type,timestamp)",
    "binance_pairs": "pairtextnotnull,base_assettextnotnull,quote_assettextnotnull,locationtextnotnull,foreignkey(base_asset)referencesassets(identifier)onupdatecascadeondeletecascade,foreignkey(quote_asset)referencesassets(identifier)onupdatecascadeondeletecascade,primarykey(pair,location)",
    "address_book": "addresstextnotnull,blockchaintextnotnull,nametextnotnull,primarykey(address,blockchain)",
    "custom_assets": "identifiertextnotnullprimarykey,notestext,typetextnotnullcollatenocase,foreignkey(identifier)referencesassets(identifier)onupdatecascadeondeletecascade",
    "asset_collections": "idintegerprimarykey,nametextnotnull,symboltextnotnull,main_assettextnotnullunique,foreignkey(main_asset)referencesassets(identifier)onupdatecascadeondeletecascade,unique(name,symbol)",
    "general_cache": "keytextnotnull,valuetextnotnull,last_queried_tsintegernotnull,primarykey(key,value)",
    "unique_cache": "keytextnotnullprimarykey,valuetextnotnull,last_queried_tsintegernotnull",
    "contract_abi": "idintegernotnullprimarykey,valuetextnotnullunique,nametext",
    "contract_data": "addressvarchar[42]notnull,chain_idintegernotnull,abiintegernotnull,deployed_blockinteger,foreignkey(abi)referencescontract_abi(id)onupdatecascadeondeletesetnull,primarykey(address,chain_id)",
    "default_rpc_nodes": "identifierintegernotnullprimarykey,nametextnotnull,endpointtextnotnull,ownedintegernotnullcheck(ownedin(0,1)),activeintegernotnullcheck(activein(0,1)),weighttextnotnull,blockchaintextnotnull",
    "location_asset_mappings": "locationtext,exchange_symboltextnotnull,local_idtextnotnullcollatenocase,unique(location,exchange_symbol)",
    "location_unsupported_assets": "locationchar(1)notnull,exchange_symboltextnotnull,unique(location,exchange_symbol)",
}
