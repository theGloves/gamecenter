服务器地址: http://<server-url>


## 用户
### POST /v1/user/register
用户注册
#### 入参
```javascript
{
	"username": "test" // 用户名
}
```
#### 出参
```javascript
{
	"code": 200 成功 500 失败
	"msg": "" 补充信息
	"data":{
		"uid": "e7fcbc52-1a5b-11ea-8e01-d46a6abb01c5"
	}
}
```

### GET /v1/user/login
用户登录（假登录，主要获取uid）
#### 入参 - url参数
```javascript
{
	"username": "test" // 用户名
}
```
#### 出参
```javascript
{
	"code": 200 成功 500 失败
	"msg": "" 补充信息
	"data":{
		"uid": "e7fcbc52-1a5b-11ea-8e01-d46a6abb01c5"
	}
}
```


## 房间
### GET /v1/room/rooms
获取房间列表
#### 入参
无
#### 出参
```javascript
{
  "code": 200,
  "data": {
    "room_list": [
      {
        "creator": {
          "id": "20d57ea4-1a54-11ea-8e01-d46a6abb01c5",
          "username": "test"
        },
        "id": 1,
        "participarot": null
      },
      {
        "creator": {
          "id": "20d57ea4-1a54-11ea-8e01-d46a6abb01c5",
          "username": "test"
        },
        "id": 2,
        "participarot": null
      },
    ]
  },
  "msg": null
}
```

### GET /v1/room/<int:rid>
获取某个房间的详细信息
#### 入参
无
#### 出参
```javascript
{
	"code": 200,
	"data": {
		"creator": {
			"id": "20d57ea4-1a54-11ea-8e01-d46a6abb01c5",
			"username": "test"
		},
		"id": 1,
		"participarot": null
		}
	},
	"msg": null
}
```

### GET /v1/room/<int:rid>/status
获取该房间的对局情况
#### 入参
无
#### 出参
```javascript
{
  "code": 200,
  "data": {
    "room_list": [
      {
        "creator": {
          "id": "20d57ea4-1a54-11ea-8e01-d46a6abb01c5",
          "username": "test"
        },
        "id": 1,
        "participarot": null
      },
      {
        "creator": {
          "id": "20d57ea4-1a54-11ea-8e01-d46a6abb01c5",
          "username": "test"
        },
        "id": 2,
        "participarot": null
      },
    ]
  },
  "msg": null
}
```

### GET /v1/room/<int:rid>
获取某个房间的详细信息
#### 入参
无
#### 出参
```javascript
{
	"code": 200,
	"data": {
		"is_gaming": bool 
    		"is_end": bool
    		
		//如果is_end为True，则有winner&msg
    		"winner": 返回获胜方id
    		"msg": str获胜原因
    
    		//如果is_gaming为True则有chess_board
    		"chess_board": [][]int
	},
	"msg": null
}
```
### POST /v1/room/createroom
创建房间
#### 入参
无
#### 出参
```javascript
{
	"code": 200,
	"data": {
		"room_id": int // 房间编号
	},
	"msg": null
}
```

### POST /v1/room/joingame
房主开始游戏
#### 入参
```javascript
{
	"user_id": //待加入的用户id
	"room_id":// 待加入的房间id
}
```
#### 出参
```javascript
{
	"code": 200,
	"data": {
	},
	"msg": null
}
```

### POST /v1/room/<int:rid>/startgame
房主开始游戏
#### 入参
无
#### 出参
```javascript
{
	"code": 200,
	"data": {
	},
	"msg": null
}
```

### POST /v1/room/joingame
玩家加入游戏，第一个加入的玩家为房主，执黑棋
#### 入参
```javascript
{
	"code": 200,
	"data": {
	},
	"msg": null
}
```
#### 出参
```javascript
{
	"code": 200,
	"data": {
	},
	"msg": null
}
```

### POST /v1/room/quitgame
玩家退出房间，如果为房主则房主禅让
#### 入参
```javascript
{
	"code": 200,
	"data": {
	},
	"msg": null
}
```
#### 出参
```javascript
{
	"code": 200,
	"data": {
	},
	"msg": null
}
```

### POST /v1/room/dropchess
轮流下棋
#### 入参
```javascript
{
	"user_id": //待加入的用户id
	"room_id":// 待加入的房间id
	"x"://落子横坐标
	"y"://落子纵坐标
}
```
#### 出参
```javascript
{
	"code": 200,
	"data": {
	},
	"msg": null
}
```

