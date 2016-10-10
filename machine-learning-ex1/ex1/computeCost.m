function J = computeCost(X, y, theta)

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;

h = X*theta
J = 1/(2*m) * sum(( h-y).^2)

end
