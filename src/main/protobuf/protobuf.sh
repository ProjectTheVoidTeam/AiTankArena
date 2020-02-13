#rm -rf ../java/message/
protoc -I=./ --java_out=../java/ --python_betterproto_out=../python/arena_lib --csharp_out=../unity/Assets/Script/Protobuf ./*.proto
#cp ./*.proto ../javascript/protobuf