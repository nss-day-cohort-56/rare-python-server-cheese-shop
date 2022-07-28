-- FULL RESET/SCORCHED EARTH FOR DB. Will keep this file updated as DB needs evolve.
-- RUN ALL CODE BELOW FOR DB RESET/DEFAULT DATA

DROP TABLE Users;
DROP TABLE Tags;
DROP TABLE Subscriptions;
DROP TABLE Reactions;
DROP TABLE Posts;
DROP TABLE PostTags;
DROP TABLE PostReactions;
DROP TABLE DemotionQueue;
DROP TABLE Comments;
DROP TABLE Categories;

CREATE TABLE "Users" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "first_name" varchar,
  "last_name" varchar,
  "email" varchar,
  "bio" varchar,
  "username" varchar,
  "password" varchar,
  "profile_image_url" varchar,
  "created_on" date,
  "active" bit,
  "is_staff" bit
);

CREATE TABLE "DemotionQueue" (
  "action" varchar,
  "admin_id" INTEGER,
  "approver_one_id" INTEGER,
  FOREIGN KEY(`admin_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`approver_one_id`) REFERENCES `Users`(`id`),
  PRIMARY KEY (action, admin_id, approver_one_id)
);


CREATE TABLE "Subscriptions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "follower_id" INTEGER,
  "author_id" INTEGER,
  "created_on" date,
  FOREIGN KEY(`follower_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Posts" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "category_id" INTEGER,
  "title" varchar,
  "publication_date" date,
  "image_url" varchar,
  "content" varchar,
  "approved" bit,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Comments" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "author_id" INTEGER,
  "content" varchar,
  "publication_date" date,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Reactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar,
  "image_url" varchar
);

CREATE TABLE "PostReactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "reaction_id" INTEGER,
  "post_id" INTEGER,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`reaction_id`) REFERENCES `Reactions`(`id`),
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`)
);

CREATE TABLE "Tags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);

CREATE TABLE "PostTags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "tag_id" INTEGER,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
);

CREATE TABLE "Categories" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);


INSERT INTO Categories ('label') VALUES ('News');
INSERT INTO `Categories` VALUES (null, 'Rants');
INSERT INTO `Categories` VALUES (null, 'Self-Help');

INSERT INTO Tags ('label') VALUES ('JavaScript');
INSERT INTO `Tags` VALUES (null, 'Uplifting');
INSERT INTO `Tags` VALUES (null, 'Instructional');
INSERT INTO `Tags` VALUES (null, 'Demoralizing');

INSERT INTO Reactions ('label', 'image_url') VALUES ('happy', 'https://freepngimg.com/thumb/emoji/47416-2-smiley-image-free-png-hq.png');
INSERT INTO Reactions ('label', 'image_url') VALUES ('laugh-cry', 'https://freepngimg.com/thumb/emoji/5-2-face-with-tears-of-joy-emoji-png.png');
INSERT INTO Reactions ('label', 'image_url') VALUES ('crying', 'https://freepngimg.com/thumb/emoji/11-2-loudly-crying-emoji-png.png');
INSERT INTO Reactions ('label', 'image_url') VALUES ('fire', 'https://freepngimg.com/thumb/emoji/58685-apple-color-symbol-fire-shape-iphone-emoji.png');
INSERT INTO Reactions ('label', 'image_url') VALUES ('pirate', 'https://freepngimg.com/thumb/emoji/65088-emoticon-piracy-smiley-pirate-emoji-png-image-high-quality.png');

INSERT INTO Users ('first_name', 'last_name', 'email', 'bio', 'username', 'password', 'profile_image_url', 'created_on', 'active', 'is_staff') VALUES ('Testy', 'Testerson', 'testing@tester.com', 'I am a dynamic placeholder bot who likes a stiff negroni and long walks on the beach', 'testrr42069', 'password', NULL, '2022-07-27T20:35:03.840Z', 1, 0);
INSERT INTO Users ('first_name', 'last_name', 'email', 'bio', 'username', 'password', 'profile_image_url', 'created_on', 'active', 'is_staff') VALUES ('Donny', 'Osmund', 'joe@jatatdc.com', 'I am maybe the most famous Mormon there is', 'donnyboi', 'password', NULL, '2022-07-27T20:35:03.840Z', 1, 0);
INSERT INTO Users ('first_name', 'last_name', 'email', 'bio', 'username', 'password', 'profile_image_url', 'created_on', 'active', 'is_staff') VALUES ('Bill', 'Lumburgh', 'burgh@initech.com', 'Time theft is a legitimate threat to corporate shareholders everywhere', 'bizman9472', 'password', NULL, '2022-07-27T20:35:03.840Z', 1, 1);

INSERT INTO `Posts` VALUES (null, 1, 1, 'The Legend of Testy', '2022-07-27T20:35:03.840Z', 'https://sjo.com/wp-content/uploads/2018/04/mountaintopview-540x280.jpg', 'This is the story of my climb from a simple data placeholder to an all-powerful oil and gas magnate', 1);
INSERT INTO `Posts` VALUES (null, 2, 2, 'Sing it, sister', '2022-07-27T20:35:03.840Z', 'https://media.wkyc.com/assets/WKYC/images/28739739-968e-4774-ac4f-3093aaec3870/28739739-968e-4774-ac4f-3093aaec3870_1140x641.jpg', 'I love my sister. But for the record, I am better.', 1);
INSERT INTO `Posts` VALUES (null, 1, 3, 'Testy-fy', '2022-07-27T20:35:03.840Z', 'https://i.ytimg.com/vi/j_zyb-XXWz0/hqdefault.jpg', "Cuz it's right outside yer door", 1);

INSERT INTO PostTags ('post_id', 'tag_id') VALUES (1, 2);
INSERT INTO PostTags ('post_id', 'tag_id') VALUES (1, 3);
INSERT INTO PostTags ('post_id', 'tag_id') VALUES (2, 2);
INSERT INTO PostTags ('post_id', 'tag_id') VALUES (2, 4);

INSERT INTO Comments ('post_id', 'author_id', 'content', 'publication_date') VALUES (1, 2, 'How inspiring!', '2022-07-27T20:35:03.840Z');
INSERT INTO Comments ('post_id', 'author_id', 'content', 'publication_date') VALUES (2, 1, 'How sassy!', '2022-07-27T20:35:03.840Z');
INSERT INTO Comments ('post_id', 'author_id', 'content', 'publication_date') VALUES (2, 3, 'Yeaaaaaaaaaaah...', '2022-07-27T20:35:03.840Z');

