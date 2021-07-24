import json

# JSON
# JavaScript Object Notation
spotify_data = json.loads("{\"artists\":{\"href\":\"https://api.spotify.com/v1/search?query=lil&type=artist&offset=0&limit=20\",\"items\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/4O15NlyKLIASxsJ0PrXPfz\"},\"followers\":{\"href\":null,\"total\":553063},\"genres\":[\"dwn trap\",\"pop rap\",\"rap\",\"trap music\"],\"href\":\"https://api.spotify.com/v1/artists/4O15NlyKLIASxsJ0PrXPfz\",\"id\":\"4O15NlyKLIASxsJ0PrXPfz\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/8c02344d1cb9069a5a2a9d1e860dc88b04088549\",\"width\":640},{\"height\":320,\"url\":\"https://i.scdn.co/image/28ac78387ad26048ccab0b671cbaddb30a2b52da\",\"width\":320},{\"height\":160,\"url\":\"https://i.scdn.co/image/6b074e198860470024e57ebbc1dda9f58088c506\",\"width\":160}],\"name\":\"Lil Uzi Vert\",\"popularity\":90,\"type\":\"artist\",\"uri\":\"spotify:artist:4O15NlyKLIASxsJ0PrXPfz\"},{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/6icQOAFXDZKsumw3YXyusw\"},\"followers\":{\"href\":null,\"total\":415708},\"genres\":[\"dwn trap\",\"pop rap\",\"rap\",\"trap music\"],\"href\":\"https://api.spotify.com/v1/artists/6icQOAFXDZKsumw3YXyusw\",\"id\":\"6icQOAFXDZKsumw3YXyusw\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/d374bb14a07c17c1a23c7201916850ff4307d4a3\",\"width\":640},{\"height\":320,\"url\":\"https://i.scdn.co/image/9ca085e2d83f6c8df26ef42dcc53ae68129309d3\",\"width\":320},{\"height\":160,\"url\":\"https://i.scdn.co/image/e1924f9cdc82bd2a997e235cb488659a4da74b33\",\"width\":160}],\"name\":\"Lil Yachty\",\"popularity\":86,\"type\":\"artist\",\"uri\":\"spotify:artist:6icQOAFXDZKsumw3YXyusw\"},{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/55Aa2cqylxrFIXC767Z865\"},\"followers\":{\"href\":null,\"total\":3310974},\"genres\":[\"dwn trap\",\"hip hop\",\"pop christmas\",\"pop rap\",\"rap\",\"trap music\"],\"href\":\"https://api.spotify.com/v1/artists/55Aa2cqylxrFIXC767Z865\",\"id\":\"55Aa2cqylxrFIXC767Z865\",\"images\":[{\"height\":1239,\"url\":\"https://i.scdn.co/image/cf012139c3b8681b46a66bae70558a8a336ab231\",\"width\":1000},{\"height\":793,\"url\":\"https://i.scdn.co/image/fffd48d60e27901f6e9ce99423f045cb2b893944\",\"width\":640},{\"height\":248,\"url\":\"https://i.scdn.co/image/bf03141629c202e94b206f1374a39326a9d8c6ca\",\"width\":200},{\"height\":79,\"url\":\"https://i.scdn.co/image/521f99f2469883b8806a69a3a2487fdd983bd621\",\"width\":64}],\"name\":\"Lil Wayne\",\"popularity\":90,\"type\":\"artist\",\"uri\":\"spotify:artist:55Aa2cqylxrFIXC767Z865\"},{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/1tqhsYv8yBBdwANFNzHtcr\"},\"followers\":{\"href\":null,\"total\":395982},\"genres\":[\"dwn trap\",\"hip hop\",\"pop rap\",\"rap\"],\"href\":\"https://api.spotify.com/v1/artists/1tqhsYv8yBBdwANFNzHtcr\",\"id\":\"1tqhsYv8yBBdwANFNzHtcr\",\"images\":[{\"height\":1000,\"url\":\"https://i.scdn.co/image/a9c000526b14038b1fe69c72b0775f125bdf08af\",\"width\":1000},{\"height\":640,\"url\":\"https://i.scdn.co/image/31eac6ae8bdd6909236b5fd729d17406cc794e2d\",\"width\":640},{\"height\":200,\"url\":\"https://i.scdn.co/image/24dcb67ddd3afc794a4b1dab4cc1a47035a0beab\",\"width\":200},{\"height\":64,\"url\":\"https://i.scdn.co/image/2d2ebd85f676535129dbb7c3a4bb96e7bfd940a7\",\"width\":64}],\"name\":\"Lil Dicky\",\"popularity\":72,\"type\":\"artist\",\"uri\":\"spotify:artist:1tqhsYv8yBBdwANFNzHtcr\"},{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/6z7xFFHxYkE9t8bwIF0Bvg\"},\"followers\":{\"href\":null,\"total\":301830},\"genres\":[\"crunk\",\"deep pop r&b\",\"deep southern trap\",\"deep trap\",\"dirty south rap\",\"dwn trap\",\"gangster rap\",\"pop rap\",\"rap\",\"southern hip hop\",\"trap music\"],\"href\":\"https://api.spotify.com/v1/artists/6z7xFFHxYkE9t8bwIF0Bvg\",\"id\":\"6z7xFFHxYkE9t8bwIF0Bvg\",\"images\":[{\"height\":667,\"url\":\"https://i.scdn.co/image/47ee27a356d5c7b9ede7149f98884c98bccd7d8c\",\"width\":1000},{\"height\":427,\"url\":\"https://i.scdn.co/image/28e4dab7b71f765fd05ae82c4ce99ce848baa68b\",\"width\":640},{\"height\":133,\"url\":\"https://i.scdn.co/image/c918601cf3790918aa02354fe8d5439c0e7dddec\",\"width\":200},{\"height\":43,\"url\":\"https://i.scdn.co/image/e9cd16d9b3c3063d0c6a69a0f2a5bfc78eb3439d\",\"width\":64}],\"name\":\"Boosie Badazz\",\"popularity\":70,\"type\":\"artist\",\"uri\":\"spotify:artist:6z7xFFHxYkE9t8bwIF0Bvg\"},{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/7sfl4Xt5KmfyDs2T3SVSMK\"},\"followers\":{\"href\":null,\"total\":309046},\"genres\":[\"crunk\",\"dirty south rap\",\"gangster rap\",\"hip hop\",\"hip pop\",\"pop rap\",\"rap\",\"southern hip hop\",\"trap music\"],\"href\":\"https://api.spotify.com/v1/artists/7sfl4Xt5KmfyDs2T3SVSMK\",\"id\":\"7sfl4Xt5KmfyDs2T3SVSMK\",\"images\":[{\"height\":664,\"url\":\"https://i.scdn.co/image/c9a01130f6d9e7178ac84e35f291de5f2741483b\",\"width\":1000},{\"height\":425,\"url\":\"https://i.scdn.co/image/33cf0401b1089d239ddade0e8d77d3cdd061ce5d\",\"width\":640},{\"height\":133,\"url\":\"https://i.scdn.co/image/f11feefbacc8d4b15a3889e37a5802ce95422977\",\"width\":200},{\"height\":43,\"url\":\"https://i.scdn.co/image/5964643cd5e0009ac7bc66d05c970aee24697f96\",\"width\":64}],\"name\":\"Lil Jon\",\"popularity\":76,\"type\":\"artist\",\"uri\":\"spotify:artist:7sfl4Xt5KmfyDs2T3SVSMK\"},{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3hcs9uc56yIGFCSy9leWe7\"},\"followers\":{\"href\":null,\"total\":216080},\"genres\":[\"deep pop r&b\",\"deep trap\",\"deep underground hip hop\",\"drill\",\"dwn trap\",\"gangster rap\",\"hip hop\",\"pop rap\",\"rap\",\"southern hip hop\",\"trap music\",\"underground hip hop\"],\"href\":\"https://api.spotify.com/v1/artists/3hcs9uc56yIGFCSy9leWe7\",\"id\":\"3hcs9uc56yIGFCSy9leWe7\",\"images\":[{\"height\":482,\"url\":\"https://i.scdn.co/image/8ec7486ace06996b8b9aa08228dd10a37153d139\",\"width\":724},{\"height\":426,\"url\":\"https://i.scdn.co/image/869b4ae8e7fc253adc96fea5b9c75a27fc1ac498\",\"width\":640},{\"height\":133,\"url\":\"https://i.scdn.co/image/e07ba06307086c181fb41c80979ecf33d0edd772\",\"width\":200},{\"height\":43,\"url\":\"https://i.scdn.co/image/47b22dcf9cbcf53a6a1d842044bade9390e36b8a\",\"width\":64}],\"name\":\"Lil Durk\",\"popularity\":66,\"type\":\"artist\",\"uri\":\"spotify:artist:3hcs9uc56yIGFCSy9leWe7\"},{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/5QdEbQJ3ylBnc3gsIASAT5\"},\"followers\":{\"href\":null,\"total\":105513},\"genres\":[\"deep pop r&b\",\"deep trap\",\"drill\",\"dwn trap\",\"rap\",\"southern hip hop\",\"trap music\",\"underground hip hop\"],\"href\":\"https://api.spotify.com/v1/artists/5QdEbQJ3ylBnc3gsIASAT5\",\"id\":\"5QdEbQJ3ylBnc3gsIASAT5\",\"images\":[{\"height\":1000,\"url\":\"https://i.scdn.co/image/c1aee89bdd376783d50dabf8f271a1a1183c8802\",\"width\":1000},{\"height\":640,\"url\":\"https://i.scdn.co/image/bc3c8a6d1cc9d67ba360c4225e5f3c2c6eba05ae\",\"width\":640},{\"height\":200,\"url\":\"https://i.scdn.co/image/37fcc09778ba8159adaa1bb74556ed31a3662b7f\",\"width\":200},{\"height\":64,\"url\":\"https://i.scdn.co/image/15cc3698c7249206797a0b77d94b96e21390310e\",\"width\":64}],\"name\":\"G Herbo\",\"popularity\":66,\"type\":\"artist\",\"uri\":\"spotify:artist:5QdEbQJ3ylBnc3gsIASAT5\"},{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/6L3x3if9RVimruryD9LoFb\"},\"followers\":{\"href\":null,\"total\":99396},\"genres\":[\"chicano rap\",\"latin hip hop\",\"west coast rap\"],\"href\":\"https://api.spotify.com/v1/artists/6L3x3if9RVimruryD9LoFb\",\"id\":\"6L3x3if9RVimruryD9LoFb\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/cfd7070569577277b3b7465c3ec77ecc936d706c\",\"width\":640},{\"height\":320,\"url\":\"https://i.scdn.co/image/6c8e6f68bb7dcb1281c993bcda4e9968d3e752e2\",\"width\":320},{\"height\":160,\"url\":\"https://i.scdn.co/image/83af28eb724562b826c87839fc3d51c274009287\",\"width\":160}],\"name\":\"King Lil G\",\"popularity\":63,\"type\":\"artist\",\"uri\":\"spotify:artist:6L3x3if9RVimruryD9LoFb\"},{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/4uSN8Y3kgFNVULUWsZEAVW\"},\"followers\":{\"href\":null,\"total\":83640},\"genres\":[\"deep trap\",\"drill\",\"dwn trap\",\"rap\",\"southern hip hop\",\"trap music\",\"underground hip hop\"],\"href\":\"https://api.spotify.com/v1/artists/4uSN8Y3kgFNVULUWsZEAVW\",\"id\":\"4uSN8Y3kgFNVULUWsZEAVW\",\"images\":[{\"height\":1000,\"url\":\"https://i.scdn.co/image/07c75abe717a9b704083ef38c4446abbff10fda5\",\"width\":1000},{\"height\":640,\"url\":\"https://i.scdn.co/image/1903fd19c7279418c71da62aa02ce47cccf63e52\",\"width\":640},{\"height\":200,\"url\":\"https://i.scdn.co/image/9c37f8c40ab3594de42f1861f592f558f91d0f51\",\"width\":200},{\"height\":64,\"url\":\"https://i.scdn.co/image/efba595d34603b014b125d65f7851103185158b4\",\"width\":64}],\"name\":\"Lil Bibby\",\"popularity\":62,\"type\":\"artist\",\"uri\":\"spotify:artist:4uSN8Y3kgFNVULUWsZEAVW\"},{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3ciRvbBIVz9fBoPbtSYq4x\"},\"followers\":{\"href\":null,\"total\":22395},\"genres\":[],\"href\":\"https://api.spotify.com/v1/artists/3ciRvbBIVz9fBoPbtSYq4x\",\"id\":\"3ciRvbBIVz9fBoPbtSYq4x\",\"images\":[{\"height\":500,\"url\":\"https://i.scdn.co/image/aafc4156598fa9f8f052ec5687e648ba9120f07e\",\"width\":554},{\"height\":181,\"url\":\"https://i.scdn.co/image/148d89de19ef829de62200502db86c49ba54fc9b\",\"width\":200},{\"height\":58,\"url\":\"https://i.scdn.co/image/7ff7530a27f867705a42387ff101bd8c22d91029\",\"width\":64}],\"name\":\"Lil Jon & The East Side Boyz\",\"popularity\":65,\"type\":\"artist\",\"uri\":\"spotify:artist:3ciRvbBIVz9fBoPbtSYq4x\"},{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/5einkgXXrjhfYCyac1FANB\"},\"followers\":{\"href\":null,\"total\":52827},\"genres\":[\"crunk\",\"deep trap\",\"dirty south rap\",\"gangster rap\",\"pop rap\",\"rap\",\"southern hip hop\",\"trap music\",\"wrestling\"],\"href\":\"https://api.spotify.com/v1/artists/5einkgXXrjhfYCyac1FANB\",\"id\":\"5einkgXXrjhfYCyac1FANB\",\"images\":[{\"height\":300,\"url\":\"https://i.scdn.co/image/722a084be153a03ca1bfb0c1e7c83bd4d37db156\",\"width\":225},{\"height\":267,\"url\":\"https://i.scdn.co/image/4555e3ba2ce615db26fe7c686119310121f13c43\",\"width\":200},{\"height\":85,\"url\":\"https://i.scdn.co/image/5100ab1000dfd4fee375416ac4d4bb252d8c5994\",\"width\":64}],\"name\":\"Lil Scrappy\",\"popularity\":57,\"type\":\"artist\",\"uri\":\"spotify:artist:5einkgXXrjhfYCyac1FANB\"},{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/42FaEHFfyxTdZQ5W28dXnj\"},\"followers\":{\"href\":null,\"total\":47718},\"genres\":[\"deep southern trap\",\"deep trap\",\"dirty south rap\",\"drill\",\"dwn trap\",\"rap\",\"trap music\",\"west coast trap\"],\"href\":\"https://api.spotify.com/v1/artists/42FaEHFfyxTdZQ5W28dXnj\",\"id\":\"42FaEHFfyxTdZQ5W28dXnj\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/ddca5a96819f9b87facfeae0e6bb848872adf6a6\",\"width\":640},{\"height\":300,\"url\":\"https://i.scdn.co/image/5351255232ba825391cb5122f925ecddccf7edf9\",\"width\":300},{\"height\":64,\"url\":\"https://i.scdn.co/image/f51c6379bcefaf182526ea12d61ba7374abdfed0\",\"width\":64}],\"name\":\"Lil Snupe\",\"popularity\":55,\"type\":\"artist\",\"uri\":\"spotify:artist:42FaEHFfyxTdZQ5W28dXnj\"},{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/1bPxKZtCdjB1aj1csBJpdS\"},\"followers\":{\"href\":null,\"total\":35935},\"genres\":[\"deep trap\",\"drill\",\"dwn trap\",\"rap\",\"southern hip hop\",\"trap music\",\"underground hip hop\"],\"href\":\"https://api.spotify.com/v1/artists/1bPxKZtCdjB1aj1csBJpdS\",\"id\":\"1bPxKZtCdjB1aj1csBJpdS\",\"images\":[{\"height\":1000,\"url\":\"https://i.scdn.co/image/ab3d68c090cadf191a1ac911c2dc3384d6da3f50\",\"width\":1000},{\"height\":640,\"url\":\"https://i.scdn.co/image/6502e44ea2ccd2bd7db7d95bf4375235174f98a8\",\"width\":640},{\"height\":200,\"url\":\"https://i.scdn.co/image/a6b52df4eeb4f61a61e58c41f46d3dfa90d2fa75\",\"width\":200},{\"height\":64,\"url\":\"https://i.scdn.co/image/003fe68d07f91bd6511951ae2fe1a0bf757aab2e\",\"width\":64}],\"name\":\"Lil Reese\",\"popularity\":56,\"type\":\"artist\",\"uri\":\"spotify:artist:1bPxKZtCdjB1aj1csBJpdS\"},{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/7352aRY2mqSxBZwzUb6LmA\"},\"followers\":{\"href\":null,\"total\":160682},\"genres\":[\"crunk\",\"dance pop\",\"deep pop r&b\",\"dirty south rap\",\"hip hop\",\"hip pop\",\"pop\",\"pop rap\",\"r&b\",\"rap\",\"southern hip hop\",\"trap music\",\"urban contemporary\"],\"href\":\"https://api.spotify.com/v1/artists/7352aRY2mqSxBZwzUb6LmA\",\"id\":\"7352aRY2mqSxBZwzUb6LmA\",\"images\":[{\"height\":1500,\"url\":\"https://i.scdn.co/image/f67a804bc8323d2b5bf616926561a072649f15e4\",\"width\":1000},{\"height\":960,\"url\":\"https://i.scdn.co/image/d37c3c8cec7b1d0440d1d1cadafc27843abc632f\",\"width\":640},{\"height\":300,\"url\":\"https://i.scdn.co/image/2710d85618fb6df29f2cd1d64e38d65cfe33800b\",\"width\":200},{\"height\":96,\"url\":\"https://i.scdn.co/image/c7395d3da5037bb7f94bd01a8dfcac4b0e12d1ff\",\"width\":64}],\"name\":\"Bow Wow\",\"popularity\":62,\"type\":\"artist\",\"uri\":\"spotify:artist:7352aRY2mqSxBZwzUb6LmA\"},{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/7B7TGqQe7QTVm2U6q8jzk1\"},\"followers\":{\"href\":null,\"total\":50034},\"genres\":[\"chicano rap\",\"g funk\",\"gangster rap\",\"latin hip hop\"],\"href\":\"https://api.spotify.com/v1/artists/7B7TGqQe7QTVm2U6q8jzk1\",\"id\":\"7B7TGqQe7QTVm2U6q8jzk1\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/35e6b03d8937bf5ab910a2f5ba11f9a92e9b51a8\",\"width\":640},{\"height\":300,\"url\":\"https://i.scdn.co/image/b9f6cb873f9ce6c79d6236b1a2ff7107c616f103\",\"width\":300},{\"height\":64,\"url\":\"https://i.scdn.co/image/b877bfe4778d1d560694bdbce3ec992762acb002\",\"width\":64}],\"name\":\"Lil Rob\",\"popularity\":54,\"type\":\"artist\",\"uri\":\"spotify:artist:7B7TGqQe7QTVm2U6q8jzk1\"},{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/1grI9x4Uzos1Asx8JmRW6T\"},\"followers\":{\"href\":null,\"total\":31062},\"genres\":[\"crunk\",\"deep southern trap\",\"deep trap\",\"dirty south rap\",\"gangster rap\",\"pop rap\",\"rap\",\"southern hip hop\",\"trap music\"],\"href\":\"https://api.spotify.com/v1/artists/1grI9x4Uzos1Asx8JmRW6T\",\"id\":\"1grI9x4Uzos1Asx8JmRW6T\",\"images\":[{\"height\":1024,\"url\":\"https://i.scdn.co/image/3e53d37d29794eccb5fc9744b962df8f2c2b1725\",\"width\":680},{\"height\":964,\"url\":\"https://i.scdn.co/image/82bb674230d0b08e5c82e10dfe175759581e7800\",\"width\":640},{\"height\":301,\"url\":\"https://i.scdn.co/image/6f26c9f3aee5c6243f2abe210ab09446df90276b\",\"width\":200},{\"height\":96,\"url\":\"https://i.scdn.co/image/35fd540d7448475f46e06bc0b46f2ca106899910\",\"width\":64}],\"name\":\"Lil Keke\",\"popularity\":52,\"type\":\"artist\",\"uri\":\"spotify:artist:1grI9x4Uzos1Asx8JmRW6T\"},{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/21O7WwRkik43ErKppxDKJq\"},\"followers\":{\"href\":null,\"total\":48076},\"genres\":[\"crunk\",\"dirty south rap\",\"gangster rap\",\"memphis hip hop\",\"pop rap\",\"redneck\",\"southern hip hop\",\"trap music\"],\"href\":\"https://api.spotify.com/v1/artists/21O7WwRkik43ErKppxDKJq\",\"id\":\"21O7WwRkik43ErKppxDKJq\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/b3b6fb609bd2a24a44519cac74c1cc553bec0011\",\"width\":640},{\"height\":300,\"url\":\"https://i.scdn.co/image/4334a3ab5cbf8b36433d5b40ab38b4d5d903b1b8\",\"width\":300},{\"height\":64,\"url\":\"https://i.scdn.co/image/dc70f70d266520db283d45ddb3ca1687cb2b2aeb\",\"width\":64}],\"name\":\"Lil Wyte\",\"popularity\":55,\"type\":\"artist\",\"uri\":\"spotify:artist:21O7WwRkik43ErKppxDKJq\"},{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/53tjQAAoj0K3WsWGiO7mHM\"},\"followers\":{\"href\":null,\"total\":1603},\"genres\":[\"dwn trap\",\"trap music\"],\"href\":\"https://api.spotify.com/v1/artists/53tjQAAoj0K3WsWGiO7mHM\",\"id\":\"53tjQAAoj0K3WsWGiO7mHM\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/d00a4c22d2c6c899c334f1d9ee04a605b923839f\",\"width\":640},{\"height\":300,\"url\":\"https://i.scdn.co/image/699f56ca03e0844a2b35a2f697c573178e6a5076\",\"width\":300},{\"height\":64,\"url\":\"https://i.scdn.co/image/1be26c59f1639b833908afe227e750b62c26e1d3\",\"width\":64}],\"name\":\"Lil Uzi Vert Gucci Future\",\"popularity\":54,\"type\":\"artist\",\"uri\":\"spotify:artist:53tjQAAoj0K3WsWGiO7mHM\"},{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/4vIlHBnzWKbmWe8ZOkT1ZT\"},\"followers\":{\"href\":null,\"total\":2931},\"genres\":[\"west coast trap\"],\"href\":\"https://api.spotify.com/v1/artists/4vIlHBnzWKbmWe8ZOkT1ZT\",\"id\":\"4vIlHBnzWKbmWe8ZOkT1ZT\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/0df1afd92c6b1eb8981f63f8885787ca0e84cdd8\",\"width\":640},{\"height\":300,\"url\":\"https://i.scdn.co/image/9100cc514735fd962c47d2c13537a947b29cb96f\",\"width\":300},{\"height\":64,\"url\":\"https://i.scdn.co/image/01184ebe9f61b0b4fb97dbc581e5c16de72b9336\",\"width\":64}],\"name\":\"Lil Yase\",\"popularity\":49,\"type\":\"artist\",\"uri\":\"spotify:artist:4vIlHBnzWKbmWe8ZOkT1ZT\"}],\"limit\":20,\"next\":\"https://api.spotify.com/v1/search?query=lil&type=artist&offset=20&limit=20\",\"offset\":0,\"previous\":null,\"total\":4955}}")





print(spotify_data)
print(spotify_data.keys())
print(spotify_data['artists'])
print(spotify_data['artists'].keys())


