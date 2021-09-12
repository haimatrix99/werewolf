# werewolf

Game werewolf sẽ được chơi trên nền tảng discord với sự quản lý bởi Bot.
Game gồm các chức năng cơ bản: Cupid, Bảo vệ, Phù thuỷ, Thợ săn, Tiên tri, Sói thường, Sói nguyền và cuối cùng là Dân làng.
Game sẽ được bắt đầu khi một người đại điện sẽ thực hiện tạo ra các chức năng có trong game bằng lệnh $addrole sao cho game cân bằng nhất.

Sau khi đã setup xong chức năng, mọi người trong discord sẽ dùng lệnh $getrole để nhận chức năng của mình trong các chức năng đã setup.
Khi $getrole thì mọi người sẽ nhận được 1 message từ Bot thông báo chức năng của người đó là gì.
Sau khi mọi người đã $getrole hết thì game sẽ được bắt đầu tính từ đây. Nếu có đầy đủ chức năng thì thứ tự được tag sẽ như sau:
Đêm đầu tiên: Cupid -> Couple (Đêm đầu xem chức năng của nhau) -> Bảo vệ -> Đàn sói -> Sói nguyền -> Bán sói (Nếu hoá sói sẽ được gửi message riêng về cho bán sói)
-> Phù thuỷ -> Tiên tri -> Thợ săn -> Couple -> Thời gian thảo luận và vote.
Các đêm tiếp theo: Bảo vệ -> Đàn sói -> Sói nguyền -> Bán sói (Nếu hoá sói sẽ được gửi message riêng về cho bán sói)
-> Phù thuỷ -> Tiên tri -> Thợ săn -> Couple -> Thời gian thảo luận và vote.

Từng lệnh của từng chức năng sẽ được thông báo ở khi chức năng được gọi.

Game kết thúc khi số Sói bằng số Dân làng hoặc không còn Sói trong dân làng. Nếu có phe thứ 3 thì phe thứ 3 thắng khi còn 4 người.

Have fun in game! <3