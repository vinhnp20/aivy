#Source code Vietnamese

from gtts import gTTS
from playsound import playsound
import threading

#Gioi thieu

tts = gTTS('Xin chào bạn, mình là robot kể chuyện. Mình có một vài câu chuyện để kể cho bạn như sau:', lang='vi')
tts.save('xinchao.mp3')

tts = gTTS('Cuộc thi trong rừng', lang='vi')
tts.save('Truyen1_gioithieu.mp3')

tts = gTTS('Chú thỏ thông minh', lang='vi')
tts.save('Truyen2_gioithieu.mp3')

tts = gTTS('Chó sói và đàn dê', lang='vi')
tts.save('Truyen3_gioithieu.mp3')

tts = gTTS('Bạn muốn nghe chuyện nào nè !!', lang='vi')
tts.save('luachon_gioithieu.mp3')

tts = gTTS('Xin lỗi mình nghe không rõ bạn có thể nói lại được không nè !!', lang='vi')
tts.save('xinloi_gioithieu.mp3')

tts = gTTS('Đèn đã được bật !!', lang='vi')
tts.save('moden.mp3')

tts = gTTS('Đèn đã được tắt!!', lang='vi')
tts.save('tatden.mp3')

tts = gTTS('Ban có muốn nghe tiếp truyện nào nữa không hay bạn muốn mình tắt đèn để chúng ta cùng đi ngủ ??', lang='vi')
tts.save('tieptuc.mp3')


#Truyen 1 - CUOC THI TRONG RUNG
tts = gTTS('Sau đây mình sẽ kể câu truyện Cuộc thi trong rừng...... '
           'Ở một khu rừng nọ có rất nhiều các bạn động vật sống chung với nhau. '
           'Một hôm các bạn ấy tổ chức một cuộc thi xem giọng nói của ai là hay nhất và khoẻ nhất. '
           'Đầu tiên là phần biểu diễn của bạn Chó. Bạn Chó đừng lên và và cất giọng sủa “Gâu… gâu… gâu…”. '
           'Các bạn khác hỏi: “Giọng bạn như vậy có gì hay?”. Bạn Chó đáp: “Giọng của tớ là hay và khoẻ nhất. '
           'Buổi tối khi mọi người đi ngủ tớ sẽ thức để trông nhà. Nếu có người xấu vào nhà, tớ chỉ cần sủa lên họ sẽ sợ hãi mà chạy thật xa”. '
           'Các bạn khác gật gù ra vẻ đồng ý. Bạn Mèo cất tiếng nhỏ nhẹ “Meo…meooo…”. '
           'Các bạn khác ồ lên cười “Tiếng bạn nhỏ như vậy thì làm sao mà khoẻ nhất được?”. '
           'Mèo trả lời “Giọng tớ tuy nhỏ nhưng chỉ cần tớ kêu lên chuột trong nhà sợ mà chạy biến ngay”. '
           'Các bạn định quay sang tìm chuột để hỏi thì đúng là các bạn chuột sợ quá trốn hết mất rồi. '
           'Đúng là tiếng của bạn Mèo khoẻ thật. Sau bạn Mèo tới lượt phần thi của bạn Gà trống choai. Bạn gà trống đập cánh rồi dõng dạ gáy “Ò ó oooo…”. '
           'Đoạn bạn Gà khoe “Giọng tớ là khoẻ nhất vì tớ có thể đánh thức mọi người dậy. Vào buổi sáng, chỉ cần nghe tiếng gáy của tớ là tất cả sẽ bừng tỉng ngay”. '
           'Các bạn khác vỗ tay tán thưởng.Hừm, giọng bạn nào cũng hay, cũng khoẻ. '
           'Vậy bạn nào mới là người chiến thắng đây? Các bạn đang tập trung bàn luật thì từ đâu một tiếng gầm to vang lên “Gừmmmm… gừmmmm…”. '
           'Thì ra là bạn Hổ tới trễ. Các bạn khác nghe tiếng bạn Hổ gầm thì sợ quá chạy tán loạn. Bạn Hổ lên tiếng “Đừng sợ, tớ đến để thi tài mà”.'
           ' Các bạn thú thở phào rồi vỗ tay “Tiếng của bạn Hổ là khoẻ nhất rồi, bạn ấy gầm lên làm ai cũng phải sợ”.'
           'Vậy là mọi người đều đồng ý trao chiến thắng cho bạn Hổ. '
           'Bỗng dưng bạn Hổ lăn đùng ra đất giãy giụa: “Ối ối… thôi thôi… giọng bạn mới là khoẻ nhất… hãy trao phần thưởng cho bạn ấy đi. Tớ thua rồi… thua rồi…'
           '”Xung quanh các bạn đều ngạc nhiên vì chẳng nghe thấy giọng của ai cả. Bỗng từ trong lỗ tai của Hổ, một bạn chuột nhắt nhảy phóc ra kêu “Chít… chittttt…”. '
           'Chuột nói “Các bạn thấy đấy, giọng của ai cũng đều hay đều khoẻ hết. '
           'Mình dù bé xíu và chẳng khiến ai sợ, nhưng khi mình chui vào tai bạn Hổ thì bạn í lại phải chịu thua.'
           ' Chúng mình hãy luôn tự tin vào bản thân để có thể chiến thắng bất cứ điều gì nhé.Tất cả các bạn thú trong rừng đồng loạt vỗ tay và trao phần thưởng cho bạn Chuột nhắt. '
           'Và bạn Chuột lại mang phần thưởng đó chia cho tất cả các bạn trong rừng, mọi người ai nấy đều vui vẻ.', lang='vi')
tts.save('Truyen1.mp3')

#Truyen 2 - CHU THO THONG MINH
tts = gTTS('Sau đây mình sẽ kể câu truyện Chú thỏ thông minh ...... '
           'Trong khu rừng nọ có một chú Thỏ con thông minh sống cùng mẹ. Ngày ngày, Thỏ con thường tung tăng chạy ra bờ sông uống nước. Trước khi đi, bao giờ Thỏ mẹ cũng nhắc:'
           'Con phải cẩn thận nhé vì Cáo cũng hay ra sông dạo chơi lắm đấy!'
           'Một ngày nọ, vừa mới cúi xuống uống no bụng nước, Thỏ con ngẩng bất ngời thấy Cáo đang đứng gần mình và tỏ ra thân thiện:'
           'Chào Thỏ con, lên lưng anh cõng vào rừng hái nấm và hoa nào!'
           'Thỏ con chần chừ nhìn Cáo. Chợt nhớ lời mẹ dặn, Thỏ con nhanh trí giả vờ hào hứng đáp lời:'
           'Ôi thế thì thích quá anh Cáo ơi, chờ em về nhà lấy mũ đội che nắng đã nhé!'
           'Nói rồi Thỏ con nhanh nhẹn chạy ù về nhà. Thỏ con kể lại câu chuyện gặp Cáo cho mẹ nghe. Thỏ mẹ ôm Thỏ con vào lòng, khen con thông minh và nhanh trí.'
           'Trong lúc ấy, ở ngoài bờ sông, con Cáo gian ác và ngờ nghệch cứ đứng chờ mãi, chờ mãi mà không thấy Thỏ con trở lại. Cuối cùng, khi ông mặt trời đã đi ngủ, nó không thể chờ được nữa nên đành ôm cái bụng đói meo lủi thùi đi về rừng.'
           '', lang='vi')
tts.save('Truyen2.mp3')

#TRUYEN 3 - CHO SOI VA DAN DE
tts = gTTS('Sau đây mình sẽ kể câu truyện Chó sói và đàn dê ...... '
           'Ngày xửa ngày xưa, ở một khu rừng nọ có Dê mẹ và bảy chú dê con sống cùng với nhau trong một ngôi nhà nhỏ.'
           'Một hôm, dê mẹ chuẩn bị đi vào rừng để kiếm cỏ non ăn lấy sữa cho con bú. Dê mẹ bèn gọi đàn con lại dặn dò:” Các con ở nhà nhớ khóa chặt cửa đừng cho ai vào nhà nhé. Khi mẹ về, nghe thấy mẹ đọc bài thơ này thì hẵng mở cửa:'
           'Dê con ngoan ngoãn'
           'Mau mở cửa ra'
           'Mẹ đã về nhà'
           'Cho các con bú”.'
           '7 chú dê con vâng lời mẹ đóng chặt cửa. Có một con chó sói độc ác sống ở gần đó đã nghe thấy lời dặn của dê mẹ, nó nảy ra ý định lừa dê con mở cửa để vào nhà ăn thịt. Sau khi dê mẹ đi khỏi, chó sói liền đến gõ cửa rồi giả giọng dê mẹ:'
           '“Dê con ngoan ngoãn'
           'Mau mở cửa ra'
           'Mẹ đã về nhà'
           'Cho các con bú”'
           'Bảy chú dê con nhận ra giọng ồm ồm của chó sói nên đã nhất quyết không mở cửa.'
           'Một lúc sau, chó sói lại đến và gõ cửa. Lần này nó giả giọng nhẹ nhàng hơn cho giống với giọng dê mẹ.'
           'Bầy dê con bắt cho sói phải cho xem bộ móng. Khi thấy bộ móng vuốt đen xì của nó qua ô cửa sổ, bầy dê biết đó là chó sói và đuổi đi ngay.'
           'Chó sói nham hiểm liền đến tiệm bánh mua bột mỳ trắng và xoa vào móng vuốt của mình.'
           'Khi nó đến gõ cửa lần thứ ba những chú dê con nhìn thấy bộ móng màu trắng và cứ tưởng rằng đó là mẹ của mình.'
           'Dê con mở cửa cho sói vào nhà và nó lao đến và nuốt chửng cả bầy dê vào bụng, may thay chú dê bé nhất trốn thoát đươc.'
           'Khi dê mẹ vừa về đến nhà, dê út oà khóc nức nở: “Mẹ ơi, chó sói độc ác đã nuốt chửng hết các anh chị của con rồi”.Chó sói lúc nào đang ngủ say, dê mẹ liền mổ bụng nó ra. Sáu chú dê con liền chui ra. Dê mẹ bảo các con nhặt thật nhiều đá sỏi để nhét vào dạ dày nó rồi khâu bụng nó lại.Khi chó sói tỉnh dậy nó cảm thấy vô cùng khát nước, nó lần mò ra giếng uống nước.Vì trong bụng nặng trĩu toàn đá là đá nên nó bị rơi tòm xuống giếng. Thế là hết đời con sói gian ác.'
           '', lang='vi')
tts.save('Truyen3.mp3')