function [] = srmculprits(svdfile)

load(svdfile)

%parameters
pcthresh = 1; %threshold value to identify suspicious users
degthresh = 10; %minimum degree consideration

q = unique(indegs);
lq = length(q);
trackpct_indegs = sparse(lq,2);
for i = 1:lq
	deg = q(i);
	trackpct_indegs(i,1) = deg;
	indices = find(indegs == deg);
	vsub = v(indices,:);
	rdegs = sum((vsub*s).^2,2);
	trackpct_indegs(i,2) = prctile(rdegs,pcthresh);
end

q = unique(outdegs);
lq = length(q);
trackpct_outdegs = sparse(lq,2);
for i = 1:lq
	deg = q(i);
	trackpct_outdegs(i,1) = deg;
	indices = find(outdegs == deg);
	usub = u(indices,:);
	rdegs = sum((usub*s).^2,2);
	trackpct_outdegs(i,2) = prctile(rdegs,pcthresh);
end

[~,fn,~] = fileparts(svdfile)
save(strcat(fn,'.mat'),'trackpct_indegs','trackpct_outdegs','-v7.3');
disp(['degree thresholds saved in ' strcat(fn,'.mat')])


nnodes = length(indegs);
ictr = 1;
octr = 1;
isub = find(indegs > degthresh);
osub = find(outdegs > degthresh);
lisub = length(isub);
losub = length(osub);


for i = 1:lisub
        node = isub(i);
        if rec_indegs(node) < trackpct_indegs(find(trackpct_indegs(:,1) == indegs(node)),2)
                        iculprits(ictr,1) = node;
                        iculprits(ictr,2) = indegs(node);
                        ictr = ictr + 1;
        end
end

for i = 1:losub
        node = osub(i);
        if rec_outdegs(node) < trackpct_outdegs(find(trackpct_outdegs(:,1) == outdegs(node)),2)
                        oculprits(octr,1) = node;
                        oculprits(octr,2) = outdegs(node);
                        octr = octr + 1;
        end
end

save(strcat(fn,'.mat'),'iculprits','oculprits','-v7.3');
disp(['suspicious node ids saved in ' strcat(fn,'.mat')])

end
