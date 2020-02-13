package cn.teamthevoid.AiTankArenaServer.handler;

import cn.teamthevoid.AiTankArenaServer.message.operation.Operation;
import cn.teamthevoid.AiTankArenaServer.message.operation.OperationType;
import cn.teamthevoid.AiTankArenaServer.message.response.Response;
import cn.teamthevoid.AiTankArenaServer.message.response.Status;
import cn.teamthevoid.AiTankArenaServer.room.ServerState;
import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;

public abstract class OperationInboundHandlerAdapter extends ChannelInboundHandlerAdapter {

    protected ServerState serverState;

    public OperationInboundHandlerAdapter setServerState(ServerState serverState) {
        this.serverState = serverState;
        return this;
    }

    abstract OperationType getOperationType();

    abstract void channelRead(ChannelHandlerContext ctx, Operation operation);

    @Override
    public void channelRead(ChannelHandlerContext ctx, Object msg) throws Exception {
        Operation operation = (Operation) msg;
        if (operation.getType().equals(getOperationType())) {
            channelRead(ctx, operation);
        } else ctx.fireChannelRead(msg);
    }

    @Override
    public void exceptionCaught(ChannelHandlerContext ctx, Throwable cause) { // (4)
        cause.printStackTrace();
        ctx.channel().writeAndFlush(
                Response.newBuilder()
                        .setStatus(Status.SERVER_ERROR)
                        .build()
        );

//        ctx.close();
    }

}
