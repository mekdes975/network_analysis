CREATE TABLE users (
    id VARCHAR(50) PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    name VARCHAR(50),
    email VARCHAR(100),
    display_name VARCHAR(100),
    display_name_normalized VARCHAR(100),
    real_name VARCHAR(100),
    real_name_normalized VARCHAR(100)
);

CREATE TABLE channels (
    id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(50),
    created TIMESTAMP,
    creator VARCHAR(50),
    is_archived BOOLEAN,
    is_general BOOLEAN,
    topic_value VARCHAR(255),
    topic_creator VARCHAR(50),
    topic_last_set TIMESTAMP,
    purpose_value VARCHAR(255),
    purpose_creator VARCHAR(50),
    purpose_last_set TIMESTAMP
);

CREATE TABLE channel_members (
    channel_id VARCHAR(50),
    member_id VARCHAR(50),
    PRIMARY KEY (channel_id, member_id),
    FOREIGN KEY (channel_id) REFERENCES channels (id),
    FOREIGN KEY (member_id) REFERENCES users (id)
);

CREATE TABLE messages (
    client_msg_id VARCHAR(50) PRIMARY KEY,
    type VARCHAR(50),
    text TEXT,
    ts TIMESTAMP,
    msg_type VARCHAR(50),
    msg_content TEXT,
    sender_name VARCHAR(255),  -- Assuming sender_name is a user name
    msg_sent_time TIMESTAMP,
    msg_dist_type VARCHAR(50),
    time_thread_start TIMESTAMP,
    reply_count INTEGER,
    reply_users_count INTEGER,
    reply_users TEXT[],
    tm_thread_end TIMESTAMP,
    FOREIGN KEY (sender_name) REFERENCES users(user_name)  -- Assuming "user_name" is a unique identifier in the "users" table
);
