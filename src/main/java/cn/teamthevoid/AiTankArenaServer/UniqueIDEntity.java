package cn.teamthevoid.AiTankArenaServer;

import lombok.ToString;

@ToString(includeFieldNames = false)
public abstract class UniqueIDEntity implements Entity {
    private int id = -1;

    @Override
    public int hashCode() {
        return this.getID();
    }

    public int getID() {
        if (id == -1l)
            this.id = UniqueIDGenerator.getNextUniqueID();
        return id;
    }

}
