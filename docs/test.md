## API功能测试
- 创建房间  
    ```bash
    curl -i -H "Content-Type: application/json" -X POST 127.0.0.1:9051/v1/room/createroom
    ```

- 获取房间信息  
    ```bash
    curl 127.0.0.1:9051/v1/room/1/status
    ```

- 玩家1加入房间  
    ```bash
    curl -i -H "Content-Type: application/json" -X POST -d  '{"user_id":"20d57ea4-1a54-11ea-8e01-d46a6abb01c5","room_id":1}' 127.0.0.1:9051/v1/room/joingame
    ```
    
- 尝试开始游戏  
    ```bash
    curl -X POST 127.0.0.1:9051/v1/room/1/startgame
    ```

- 玩家1退出
    ```bash
    curl -i -H "Content-Type: application/json" -X POST -d  '{"user_id":"20d57ea4-1a54-11ea-8e01-d46a6abb01c5","room_id":1}' 127.0.0.1:9051/v1/room/quitgame
    ```

- 获取房间信息
    ```bash  
    curl 127.0.0.1:9051/v1/room/1/status
    ```

- 玩家1加入房间  
    ```bash
    curl -i -H "Content-Type: application/json" -X POST -d  '{"user_id":"20d57ea4-1a54-11ea-8e01-d46a6abb01c5","room_id":1}' 127.0.0.1:9051/v1/room/joingame
    ```

- 玩家2加入游戏  
    ```bash
    curl -i -H "Content-Type: application/json" -X POST -d  '{"user_id":"e7fcbc52-1a5b-11ea-8e01-d46a6abb01c5","room_id":1}' 127.0.0.1:9051/v1/room/joingame
    ```

- 开始游戏
    ```bash  
    curl -X POST 127.0.0.1:9051/v1/room/1/startgame
    ```
    
- 轮流下棋
  ```bash
    curl -i -H "Content-Type: application/json" -X POST -d  '{"user_id":"20d57ea4-1a54-11ea-8e01-d46a6abb01c5","room_id":1,"x":0,"y":0}' 127.0.0.1:9051/v1/room/dropchess
    curl -i -H "Content-Type: application/json" -X POST -d  '{"user_id":"e7fcbc52-1a5b-11ea-8e01-d46a6abb01c5","room_id":1,"x":0,"y":1}' 127.0.0.1:9051/v1/room/dropchess

    curl -i -H "Content-Type: application/json" -X POST -d  '{"user_id":"20d57ea4-1a54-11ea-8e01-d46a6abb01c5","room_id":1,"x":1,"y":0}' 127.0.0.1:9051/v1/room/dropchess
    curl -i -H "Content-Type: application/json" -X POST -d  '{"user_id":"e7fcbc52-1a5b-11ea-8e01-d46a6abb01c5","room_id":1,"x":1,"y":1}' 127.0.0.1:9051/v1/room/dropchess

    curl -i -H "Content-Type: application/json" -X POST -d  '{"user_id":"20d57ea4-1a54-11ea-8e01-d46a6abb01c5","room_id":1,"x":2,"y":0}' 127.0.0.1:9051/v1/room/dropchess
    curl -i -H "Content-Type: application/json" -X POST -d  '{"user_id":"e7fcbc52-1a5b-11ea-8e01-d46a6abb01c5","room_id":1,"x":2,"y":1}' 127.0.0.1:9051/v1/room/dropchess

    curl -i -H "Content-Type: application/json" -X POST -d  '{"user_id":"20d57ea4-1a54-11ea-8e01-d46a6abb01c5","room_id":1,"x":3,"y":0}' 127.0.0.1:9051/v1/room/dropchess
    curl -i -H "Content-Type: application/json" -X POST -d  '{"user_id":"e7fcbc52-1a5b-11ea-8e01-d46a6abb01c5","room_id":1,"x":3,"y":1}' 127.0.0.1:9051/v1/room/dropchess

    curl -i -H "Content-Type: application/json" -X POST -d  '{"user_id":"20d57ea4-1a54-11ea-8e01-d46a6abb01c5","room_id":1,"x":4,"y":0}' 127.0.0.1:9051/v1/room/dropchess
    curl 127.0.0.1:9051/v1/room/1/status
    ```