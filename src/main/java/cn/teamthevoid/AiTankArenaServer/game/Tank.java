package cn.teamthevoid.AiTankArenaServer.game;

import cn.teamthevoid.AiTankArenaServer.UniqueIDEntity;

public abstract class Tank extends UniqueIDEntity {
    public Tank(Vector2D initPostion) {

    }

    public abstract Vector2D getPosition();

    public abstract void move(Vector2D direction, float speed);
}
