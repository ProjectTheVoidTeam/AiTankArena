// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: operation.proto

package cn.teamthevoid.AiTankArenaServer.message;

public final class OperationOuterClass {
  static final com.google.protobuf.Descriptors.Descriptor
          internal_static_AiTankArenaServer_Operation_descriptor;

  public static void registerAllExtensions(
          com.google.protobuf.ExtensionRegistryLite registry) {
  }

  public static void registerAllExtensions(
          com.google.protobuf.ExtensionRegistry registry) {
    registerAllExtensions(
            (com.google.protobuf.ExtensionRegistryLite) registry);
  }

  static final
  com.google.protobuf.GeneratedMessageV3.FieldAccessorTable
          internal_static_AiTankArenaServer_Operation_fieldAccessorTable;

  static {
    java.lang.String[] descriptorData = {
            "\n\017operation.proto\022\021AiTankArenaServer\"L\n\t" +
                    "Operation\022.\n\004type\030\001 \001(\0162 .AiTankArenaSer" +
                    "ver.OperationType\022\017\n\007message\030\002 \001(\t*u\n\rOp" +
                    "erationType\022\016\n\nGET_STATUS\020\000\022\010\n\004JOIN\020\001\022\r\n" +
                    "\tAI_ACTION\020\002\022\n\n\006FRANCE\020\003\022\010\n\004HALT\020\004\022\010\n\004IN" +
                    "IT\020\005\022\n\n\006REJOIN\020\006\022\017\n\013SERVER_INFO\020\007B,\n(cn." +
                    "teamthevoid.AiTankArenaServer.messageP\001b" +
                    "\006proto3"
    };
    descriptor = com.google.protobuf.Descriptors.FileDescriptor
      .internalBuildGeneratedFileFrom(descriptorData,
              new com.google.protobuf.Descriptors.FileDescriptor[]{
              });
    internal_static_AiTankArenaServer_Operation_descriptor =
            getDescriptor().getMessageTypes().get(0);
    internal_static_AiTankArenaServer_Operation_fieldAccessorTable = new
            com.google.protobuf.GeneratedMessageV3.FieldAccessorTable(
            internal_static_AiTankArenaServer_Operation_descriptor,
            new java.lang.String[]{"Type", "Message",});
  }

  public static com.google.protobuf.Descriptors.FileDescriptor
  getDescriptor() {
    return descriptor;
  }

  private static com.google.protobuf.Descriptors.FileDescriptor
          descriptor;

  private OperationOuterClass() {
  }

  // @@protoc_insertion_point(outer_class_scope)
}
