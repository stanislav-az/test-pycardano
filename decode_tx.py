from pycardano import Transaction

tx_hex = "84ac00848258201aab4ffa64734958360989614fdc8b61657c236a54860da4cf0423ae03505b0709825820830e26f29fadcbb94f5672f22f6bf01e1adfab4336a72cd1c43144266a132d0f00825820bf349d594fe5c89817ab0761dad195baeb47ef97965257aee9346fabdedb80fc00825820c8d61c302a333d05728e560d5551259b86660685d2ab177d71e99d99b241dd9b000184a300581d7093374560a247053633443d16023a52b40dc4d2fda10f95801569a68801821a002dc6c0a2581c49d937b3714b66d95376fc7e76575ecbed4188b6e4be56527cfce7c1a148416767537461746501581c88938c50773839037610c16536b830801b82484fdc4d74a7e4c21101a146546573744333190398028201d81859011fd87b9fd8799fd8799f9f581cb12bdcb45c6b5196cf226d3207e82458de71572e7ef834a308727653581cf589d7ec4fc932e5d5e28e4127c5fb2089f587e5709dc50969a967fe581cdad699f810d1de25e7723085aa7078b863dbe82ab9c5c0c2bcff531a581c4370fa6a2550735dc748419287843073dfd7ac3cb83396629f058880ff1917701a001b77401a001b774018c8d8799f0a140aff021905dcd8799f9f581ca851fb22e72cdcc4f1f9b5f421f31338b0017d761468ece886c925fa581c096bfb3d5b0418c1c6945597e550bc67999e912d00373c89f42cf670581c393a814e52e7c36a455cbf4041525a04d3191bf21c659ff452e179a7581c21478946f112d8424f45d1663879bb591de13f401bf4588f9af28fd3ff03ffffffffa300581d7093374560a247053633443d16023a52b40dc4d2fda10f95801569a68801821a002dc6c0a2581c49d937b3714b66d95376fc7e76575ecbed4188b6e4be56527cfce7c1a14652657761726401581c88938c50773839037610c16536b830801b82484fdc4d74a7e4c21101a1465465737443330a028201d8185897d87c9fd8799f9fd8799f581cb12bdcb45c6b5196cf226d3207e82458de71572e7ef834a30872765300ffd8799f581cf589d7ec4fc932e5d5e28e4127c5fb2089f587e5709dc50969a967fe00ffd8799f581cdad699f810d1de25e7723085aa7078b863dbe82ab9c5c0c2bcff531a00ffd8799f581c4370fa6a2550735dc748419287843073dfd7ac3cb83396629f05888000ffff0affff82583900a851fb22e72cdcc4f1f9b5f421f31338b0017d761468ece886c925fa95a3b5ab9af57c7671df57db18ded08ad170294edd918a292a67bd091a004c4b4082583900a851fb22e72cdcc4f1f9b5f421f31338b0017d761468ece886c925fa95a3b5ab9af57c7671df57db18ded08ad170294edd918a292a67bd091a00130e84021a000b75fc031a0237c041081a01a9a29609a1581c49d937b3714b66d95376fc7e76575ecbed4188b6e4be56527cfce7c1a1484e6f646546656564200b582017ef4202c0c0f5d4313d17036bf25df265d42d160ee1c88754c6ad93ea408e260d81825820f009b8fed4c650cff09a0f8a0ef7a482b01b1fddc1accfb30a5d439d765588ef000e83581ca851fb22e72cdcc4f1f9b5f421f31338b0017d761468ece886c925fa581c096bfb3d5b0418c1c6945597e550bc67999e912d00373c89f42cf670581c393a814e52e7c36a455cbf4041525a04d3191bf21c659ff452e179a71082583900a851fb22e72cdcc4f1f9b5f421f31338b0017d761468ece886c925fa95a3b5ab9af57c7671df57db18ded08ad170294edd918a292a67bd091a00524801111a00370c3f12818258201aab4ffa64734958360989614fdc8b61657c236a54860da4cf0423ae03505b0700a300838258201853a275d306d2357fd4192f7b10f447eb9585352ccca98632f6ac9b5f155f4a584088aaae264749102725023b42aa7359cde3c4e2abde542f5cadf6f00536ef02d4c33430ce65843af35b27f40cbf580ea440e620a7628e399b9ad540553dca4d0a8258207e4a8b20462e63614dad4c0621e526b4ec3f8d751c15dc30ba1cf1bc8c60b8be5840e6b71f890eb65bf64257ce53d64e7e1e617f7e638b527e81cfa471ee929f84b56682515e293d4764b3c5f254ee8453929320daedc9e770dfdfa471c60877f20a82582097d1cdc1584f80256726c273e7aa659bb5e8875036f483c7e6b4e652cbbbbbe258402fa524a954a90fbb7fe891588509141afd53db94c090e131d68621837394f4d2bbac9bf39a509af13c5fdcd5003064c7d8ca7d02be43884f054847f488bc410701818201828200581ca851fb22e72cdcc4f1f9b5f421f31338b0017d761468ece886c925fa82041a01a9a2960583840002d87f80821a004e0e2f1a54849378840003d87f80821a000c94821a0f52a2f0840001d87f80821a000ac0c31a0d450a18f5f6"
tx = Transaction.from_cbor(bytes.fromhex(tx_hex))
print(tx)