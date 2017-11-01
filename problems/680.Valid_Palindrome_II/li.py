# coding=utf-8
# Author: Jianghan LI
# Question: 680.Valid_Palindrome_II
# Complexity: O(N)
# Date: 2017-09-17
# Contest50 0:23:34 － 0:37:28, 1 wrong try


class Solution(object):

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == s[::-1] and len(s) % 2:
            return True
        for i in range(len(s)):
            if s[i] != s[-(i + 1)]:
                break
        if i != 0:
            s = s[i:-i]
        return s[1:] == s[1:][::-1] or s[:-1] == s[:-1][::-1]

    def validPalindrome(self, s):
        i = 0
        while i < len(s) / 2 and s[i] == s[~i]:
            i += 1
        s = s[i:len(s) - i]
        return s[1:] == s[1:][::-1] or s[:-1] == s[:-1][::-1]

############ test case ###########
s = Solution()
print s.validPalindrome("abca")
print s.validPalindrome("vxbljyyvfqjvbfmqvrvbffseoihrkjezzbxesmiumgyadcrdyelhvliymdpzzryjezklfcjaqcfrfgbgykujbsnpehuensdruexbocpluhoagbbbotvypzboyraldceguaqnveahzxyjosldfwtehonldywseonznxmwlwmxjqpsevxaexeeyrexevozbbzdhfkmgiamoyaczkhnvkdwxgoigdsqnvoeorkqegjtgtxmkbjbmhcyhipvngimbovxqaklskibicmxhctorxwzsnrblkdzmelrdetgoffauzldmtzyeaulhbnzkifeunxqeuftwetlmxyksrmykfuvumgiifqaijfqyododzvwvuyoyihtjhzgofhgxwykssuchxdqlepphetiremmsamgqobhnwmkhzweslckkwcoauxbobeplqkpcfpcukbhucgyrwjpwmfzhitdamuavzhumfdxhwlmgcnsoiudwdhdkrybzdnierzcdsuowfxritwbzkzhlsjevouikjoxpsdnedzlcvzyhhxpvgxcmfmczgoflebeurqjddnevsreuclhnggrtcpsoadyzryoeutgjnuavghvuxtywicmnhqtzdxvvnvlrylftfufxqokqyhtydzljrqzvuvxggzgokkoqjrvcsexkxssukbrijbvggsrhrnaavkamrtmtabqyfyklreoppweplnclgeqrefsqvnkjphelqmrftpsekqnecfunuiznuurpksmmdqxfdaqczgtynhxnfculicerndrnszkefupeimnkafitkwyczerwxrikkuiarscxjtbvnulyctqltrzthvdaxbxhrzmhoqksgwxresnjwmmolmcplopobeurzfibipbhnamsojemextlbyfswtgtxjaiolptvjpredtliaydrxbthvpvqxpvukjdfpkgmftnhvmvhlncpdlyspysthfshvmqzwucpfgsivpworhizjitjjxzxoxeyeigvrzfjherehbrqzayiwyyjbmvvtfsdkblttyoqxjfnebcrjeqpyhqavnuzvydvoaccpknrfjirqyulxbubmtbwefdpjjplmqzfjxdkzqaiywfhdopinywqtfrksphdeyaprcuauawbbzdhfjwbijhtdubvcnreqnaifrxyolgodnsnokybciwtmyglryvyplbfdjpotwgnieudmxftizxrajphxxasradnswheazgwnchciwxkskdeeaqmwcnlypfezklfaxgdkyjgwisbgnkadodayoasedijscnoylrdeoghulnjroaaouezzrzlqvnhzbfdfuucudsfloevjjfrxnrctvniyxtnhslwgvsddlafkaczjwqiqlwsvgqowsxptcoqtuhfbxktgrlniwgiajngwbuihmsnfafjalwpgqnrsrpdqwjwknotwegytriyzyhkfalsfhmbclajyozpxabwgguqmfuwadpumxptyyxcmlzvxfaueavwvimkothvbcyeqqvblgdlbhjwctzzlkbqviewvccadkapsyabwthvjrggmkjayaeusnqevihcbrukpdjefzbkiutmapcnvsplnxggoxespenjsvlcqcdxdwibnbobwxzyjtckgyjewvpvyvajwdzbirbzxngcjztknxbvdhzvshfzrdbwujulfxccgjsnxtksbnspbtxumtvpchgttodkjpsbsggubkehitxhuiznvgjrluovofljbtviuylgzxrpvvwycwrseowtvxjdkidllclrqhhwtabrpxphwrrnqyhfevrlkcumfbqveatktyahyecjzbwwnmxcopicapqdvdizmywdxqrnirtlknpzqaqtlhqwhaspfvebqdntfiwhyrybvzhtqssgraixkoiravczutubbzycpcbbtxxjpbkfcqxssrclcbkaccervwmbmhjzwsyitlrracpgjgtayrqnbemjcuucqnfwnfjlavcpfiqufafajbistvatemsuzragtcejqjedqiytapgnwljqmfigtmhszbjmvugvkvmfpfteqambimfjfmzgxitghexmojkavjhfbgbjzwwfsnasohvepglzdzuqpihyxeezckwhthfukkjtfumcrfrbpycuhfssanjkhkmgvbseeegnmlfybtkdnhmmkeijjlkadbmztybnrzodwzvavpneulugadcbtkvhbqdqrpeqjblbkkehykbowwjzlkfuavyjspuwmvmsysxdbceofetcqnxbihvqlsruppmlyprlzcsdmeyityyuruxtfwmblxuuhlticpwxvfhlifeptwadppwvgoohjxijzlbcckwzahhmjehgzjlyoecwprzzhysxgayojxbffgkyilrynpeulcbqnzsawyzncuntsrzzwipmyotbzxoxckkacotecjaorevjnebrbjgurcizywpitfgnfdtwbrjwrvkmzwrlhvvhktlwkkjttjmtkcasqrhubghxomkqupniotjybmrljofeqsahwioupqgigzbedkxrriqzlphyxtplhiswinysohtzxunverewjwaktqwmqikvfzspfsidmfbqygojpmdbqcarvsoovcmhuabgsefrfqixioqacdxtbrrmezarbybodowjcaxcvrkqbgyeieqawvidspmdajnshkhuicnibepcjhypzqlfllrdqijudlffyazsscnkijpnzwfaoqweyxaatckaruygjxddarscnnjimvyshltcaesvfidsccllcndkqefxjssghugeruppmjnrvsasyziijeyxrmsqxmlkckqofytczggfbfjtcprdnlsywlyitpxxyiuedpcnbfmklxcivifxyxvqijjjzazmvbpdttwiwtqunwdwxkztcehuntzpjtovvjgomupgubmbnekmnppnhqhvhnxyojurklrmcncxkwemhszcfegljndzupcficxseaesnpyekxyyicgedclqbybhuowwayounvyblhyomfpxnvawhvfbwwzmmqnxzbxwymvqznktynljgornwnwfehblronhzdznlpkgnopfciikagsmqtiecrcgphcgtnyxxdemsisvaqedujytjkwvwvfeaqnaduwvnigplbfshgsrchmoyqefjuikgfjnydvflodmwlghblfyqvgrzhvuptntdpzultnfghdgkvnjzisjvswkxybmtpbsgjrfczmjcepbmpsmasjuxbnmnrwgkimoohqojqzukpmhjlhtvrbxlummcoupumfgohhevmrrrfwmuctyhjmipfdogjmavawcmooktjaihvyzijteilwpxrjxohobriywxidgnishvhlyskddymglyojvivjfwnhalyyebucjkkwfieonxpmwfhioarxhlfqrvhkrmgitquwjxtwyrcczjruqjjeblxztkjtzuqaoljgilirdwbvgsirqxdeqnfukabcnhsrbqzsdybthhmgedmnduorlyywfdtydfeaivzxgorzowuvtmtnxfribqklkukiwutvnitkhuehevijcrajltrzuklfgqraqbzdaykrhkbhevfzhesyojqzbntqmgekzzwmtaoytczdhccunlbczbbekupgbjrlblwddibhmoxocehweuxkxnwvzaqvyjvhcaaziaaxwoaiyyseqjecfaphlulzhjvckrazdgdrevhlffctvcgolqihphwsxixgymfxcmlrrvvvpkmhnzlrikvhmfkdhqfiwuxsaxtuhyajkkovcazuaborkqsdnfvlsjitzzzjmvkuwbubcteefvvfpprulnqvpnnxtihvyupyjzygdjgswvrupzhjbsilmvggqzgbrfgbmlnhtiegqvydjbenygdkbxydazszxuycxkkcunfddoxzzlyfclqzybgvtsiboamuomhykmyragirvagiinfosysdqjddflsuoswvayzjacqttvwecfakfntcaxumofceygtrdmfpjftxxiewigdjxbeqiwqvemnteweffofvbegbhlrmdccumgcjcutwqruilppzzxmlmyttpozmcxvuleyoizpbjgxbucwzprginumijduinwzshahwethsyjgyeopmiuqsqdskiqaxoohopkddpmjalldwkitdkrkwxzfjbxsjisykrvbtscefjqroytymodypjgujnjvusykryseorxroxescowhprhdvhdcfiuqqcotznsvqbtjhkcoajcwatxxktlriceldliluvyoayesjfkszvmxuyukkkdklbhjybdxmxwitqyatmnejderznxkxwvqjphbzzibmnyfdfxxyxcdcgcwlyuqiqefkpnohvpdqmzxcsbiunylrshlahhkusfoxvlwqtgfanbjqyeybffnneivwowovffdzhikaoliqynoletroitqludlwrvhplnsgasvprqdgmsreqgrhenopqnusyvgzuurnnpexvcxkzarqiwnlmngegurvveldhufuwnrofrxskjnmvrnwvymyfhjeqlehmkmswushcmqcpdurrxankfvcdpjszkivcxczxvrxdfgfrcxdtwhrtgfwpgduecygxgnrxbsqosfvxouanpwwwmlxxcvbonnamjjqluxjmoumqviushtpeypymzvaewygppchizwyzhksiqyzprfjenwahrpsfgfbwjzmfqvycmpvyimnmbvfzokvoenshxsivfnwwlmoqomykjdxeppngbblxvggmwojaxkgcadifolrouptefoqqsvxbxnhhgfapoujawmdmttigjdnjijdgzretxcbvngjqmtkhhunrlofzkwlnhwfefpiwxzsshufsphjmteribsqnlctvjtgfrqoybpyuagcrdnkkhgnocfgfcyukqmpsfunnoovmmykgvjxruighgbmejtoxnmpajvyiwdducmhhmcuddwiyvjapmnxotjembghgiurxjvgkymmvoonnufspmqkuycfgfconghkkndrcgauypbyoqrfgtjvtclnqsbiretmjhpsfuhsszxwipfefwhnlwkzfolrnuhhktmqjgnvbcxterzgdjijndjgittmdmwajuopafghhnxbxvsqqofetpuorlofidacgkxajowmggvxlbbgnppexdjkymoqomlwwnfvisxhsneovkozfvbmnmiyvpmcyvqfmzjwbfgfsprhawnejfrpzyqiskhzywzihcppgyweavzmypyepthsuivqmuomjxulqjjmannobvcxxlmwwwpnauoxvfsoqsbxrngxgyceudgpwfgtrhwtdxcrfgfdxrvxzcxcvikzsjpdcvfknaxrrudpcqmchsuwsmkmhelqejhfymyvwnrvmnjksxrfornwufuhdlevvrugegnmlnwiqrazkxcvxepnnruuzgvysunqponehrgqersmgdqrpvsagsnlphvrwldulqtiortelonyqiloakihzdffvowowviennffbyeyqjbnafgtqwlvxofsukhhalhsrlynuibscxzmqdpvhonpkfeqiquylwcgcdcxyxxfdfynmbizzbhpjqvwxkxnzredjenmtayqtiwxmxdbyjhblkdkkkuyuxmvzskfjseyaoyvulildlecirltkxxtawcjaockhjtbqvsnztocqquifcdhvdhrphwocsexorxroesyrkysuvjnjugjpydomytyorqjfecstbvrkysijsxbjfzxwkrkdtikwdllajmpddkpohooxaqiksdqsquimpoeygjyshtewhahszwniudjimunigrpzwcubxgjbpzioyeluvxcmzopttymlmxzzppliurqwtucjcgmuccdmrlhbgebvfoffewetnmevqwiqebxjdgiweixxtfjpfmdrtgyecfomuxactnfkafcewvttqcajzyavwsouslfddjqdsysofniigavrigarymkyhmoumaobistvgbyzqlcfsylzzxoddfnuckkxcyuxzszadyxbkdgynebjdyvqgeithnlmbgfrbgzqggvmlisbjhzpurvwsgjdgyzjypuyvhitxnnpvqnlurppfvvfeetcbubwukvmjzzztijslvfndsqkrobauzacvokkjayhutxasxuwifqhdkfmhvkirlznhmkpvvvrrlmcxfmygxixswhphiqlogcvtcfflhverdgdzarkcvjhzlulhpafcejqesyyiaowxaaizaachvjyvqazvwnxkxuewhecoxomhbiddwlblrjbgpukebbzcblnucchdzctyoatmwzzkegmqtnbzqjoysehzfvehbkhrkyadzbqarqgflkuzrtljarcjiveheuhktinvtuwikuklkqbirfxntmtvuwozrogxzviaefdytdfwyylroudnmdegmhhtbydszqbrshncbakufnqedxqrisgvbwdriligjloaquztjktzxlbejjqurjzccrywtxjwuqtigmrkhvrqflhxraoihfwmpxnoeifwkkjcubeyylahnwfjvivjoylgmyddksylhvhsingdixwyirbohoxjrxpwlietjizyvhiajtkoomcwavamjgodfpimjhytcumwfrrrmvehhogfmupuocmmulxbrvthljhmpkuzqjoqhoomikgwrnmnbxujsamspmbpecjmzcfrjgsbptmbyxkwsvjsizjnvkgdhgfntluzpdtntpuvhzrgvqyflbhglwmdolfvdynjfgkiujfeqyomhcrsghsfblpginvwudanqaefvwvwkjtyjudeqavsismedxxyntgchpgcrceitqmsgakiicfpongkplnzdzhnorlbhefwnwnrogjlnytknzqvmywxbzxnqmmzwwbfvhwavnxpfmoyhlbyvnuoyawwouhbybqlcdegciyyxkeypnseaesxcifcpuzdnjlgefczshmewkxcncmrlkrujoyxnhvhqhnppnmkenbmbugpumogjvvotjpztnuhectzkxwdwnuqtwiwttdpbvmzazjjjiqvxyxfivicxlkmfbncpdeuiyxxptiylwyslndrpctjfbfggzctyfoqkcklmxqsmrxyejiizysasvrnjmppureguhgssjxfeqkdncllccsdifvseactlhsyvmijnncsraddxjgyurakctaaxyewqoafwznpjikncsszayffldujiqdrllflqzpyhjcpebinciuhkhsnjadmpsdivwaqeieygbqkrvcxacjwodobybrazemrrbtxdcaqoixiqfrfsgbauhmcvoosvracqbdmpjogyqbfmdisfpszfvkiqmwqtkawjwerevnuxzthosyniwsihlptxyhplzqirrxkdebzgigqpuoiwhasqefojlrmbyjtoinpuqkmoxhgbuhrqsacktmjttjkkwltkhvvhlrwzmkvrwjrbwtdfngftipwyzicrugjbrbenjveroajcetocakkcxoxzbtoympiwzzrstnucnzywasznqbcluepnyrliykgffbxjoyagxsyhzzrpwceoyljzghejmhhazwkccblzjixjhoogvwppdawtpefilhfvxwpcitlhuuxlbmwftxuruyytiyemdsczlrpylmppurslqvhibxnqctefoecbdxsysmvmwupsjyvaufklzjwwobkyhekkblbjqeprqdqbhvktbcdaguluenpvavzwdozrnbytzmbdakljjiekmmhndktbyflmngeeesbvgmkhkjnassfhucypbrfrcmuftjkkufhthwkczeexyhipquzdzlgpevhosansfwwzjbgbfhjvakjomxehgtixgzmfjfmibmaqetfpfmvkvguvmjbzshmtgifmqjlwngpatyiqdejqjectgarzusmetavtsibjafafuqifpcvaljfnwfnqcuucjmebnqryatgjgpcarrltiyswzjhmbmwvreccakbclcrssxqcfkbpjxxtbbcpcyzbbutuzcvariokxiargssqthzvbyryhwiftndqbevfpsahwqhltqaqzpnkltrinrqxdwymzidvdqpacipocxmnwwbzjceyhaytktaevqbfmucklrvefhyqnrrwhpxprbatwhhqrlclldikdjxvtwoesrwcywvvprxzglyuivtbjlfovoulrjgvnziuhxtihekbuggsbspjkdottghcpvtmuxtbpsnbsktxnsjgccxflujuwbdrzfhsvzhdvbxnktzjcgnxzbribzdwjavyvpvwejygkctjyzxwbobnbiwdxdcqclvsjnepsexoggxnlpsvncpamtuikbzfejdpkurbchiveqnsueayajkmggrjvhtwbayspakdaccvweivqbklzztcwjhbldglbvqqeycbvhtokmivwvaeuafxvzlmcxyytpxmupdawufmquggwbaxpzoyjalcbmhfslafkhyzyirtygewtonkwjwqdprsrnqgpwlajfafnsmhiubwgnjaigwinlrgtkxbfhutqoctpxswoqgvswlqiqwjzcakfalddsvgwlshntxyinvtcrnxrfjjveolfsducuufdfbzhnvqlzrzzeuoaaorjnluhgoedrlyoncsjidesaoyadodakngbsiwgjykdgxaflkzefpylncwmqaeedkskxwichcnwgzaehwsndarsaxxhpjarxzitfxmdueingwtopjdfblpyvyrlgymtwicbykonsndogloyxrfianqerncvbudthjibwjfhdzbbwauaucrpayedhpskrftqwynipodhfwyiaqzkdxjfzqmlpjjpdfewbtmbubxluyqrijfrnkpccaovdyvzunvaqhypqejrcbenfjxqoyttlbkdsftvvmbjyywiyazqrbherehjfzrvgieyexoxzxjjtijzihrowpvisgfpcuwzqmvhsfhtsypsyldpcnlhvmvhntfmgkpfdjkuvpxqvpvhtbxrdyailtderpjvtploiajxtgtwsfybltxemejosmanhbpibifzruebopolpcmlommwjnserxwgskqohmzrhxbxadvhtzrtlqtcylunvbtjxcsraiukkirxwrezcywktifaknmiepufekzsnrdnrecilucfnxhnytgzcqadfxqdmmskpruunziunufcenqkesptfrmqlehpjknvqsferqeglcnlpewppoerlkyfyqbatmtrmakvaanrhrsggvbjirbkussxkxescvrjqokkogzggxvuvzqrjlzdythyqkoqxfuftflyrlvnvvxdztqhnmciwytxuvhgvaunjgtueoyrzydaospctrggnhlcuersvenddjqruebelfogzcmfmcxgvpxhhyzvclzdendspxojkiuovejslhzkzbwtirxfwousdczreindzbyrkdhdwduiosncgmlwhxdfmuhzvaumadtihzfmwpjwrygcuhbkucpfcpkqlpebobxuaocwkkclsewzhkmwnhboqgmasmmeritehppelqdxhcusskywxghfogzhjthiyoyuvwvzdodoyqfjiaqfiigmuvufkymrskyxmltewtfueqxnuefikznbhluaeyztmdlzuaffogtedrlemzdklbrnszwxrotchxmcibikslkaqxvobmignvpihychmbjbkmxtgtjgeqkroeovnqsdgiogxwdkvnhkzcayomaigmkfhdzbbzovexeryeexeaxvespqjxmwlwmxnznoeswydlnohetwfdlsojyxzhaevnqaugecdlaryobzpyvtobbbgaohulpcobxeurdsneuhepnsbjukygbgfrfcqajcflkzejyrzzpdmyilvhleydrcdaygmuimsexbzzejkrhioesffbvrvqmfbvjqfvyyjlbxv")


############ comments ############
# https://discuss.leetcode.com/topic/103982/python-easy-and-concise-solution
